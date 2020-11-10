import requests
import json
import pandas as pd
import time


class HubSpotDeal(object):
    """docstring for HubSpot"""
    def __init__(self, token):
        self.params = {"hapikey":token}
        self.headers = {
            'accept': "application/json",
            'content-type': "application/json"
        }
        self.pipelines = False   
    def get_company_by_name(self, name):
        url = "https://api.hubapi.com/crm/v3/objects/companies/search"
        payload = {"filterGroups":[{
             "filters":
                  [{"propertyName":"name",
                  "operator":"EQ",
                  "value":name}]
                  }],
              "sorts":[],
              "query":"",
              "properties":["name"],
              "limit":10,
              "after":0
              }
        response = requests.request("POST", url, json=payload, headers=self.headers, params=self.params)
        return response.json()

    def get_contact_by_email(self, email):
        url = "https://api.hubapi.com/crm/v3/objects/contacts/search"
        payload = {"filterGroups":[{
             "filters":
                  [{"propertyName":"email",
                  "operator":"EQ",
                  "value":email}]
                  }],
              "sorts":[],
              "query":"",
              "properties":["email"],
              "limit":10,
              "after":0
              }
        response = requests.request("POST", url, json=payload, headers=self.headers, params=self.params)
        return response.json()
    def get_deal_by_name(self, name):
        name = name.strip()
        url = "https://api.hubapi.com/crm/v3/objects/deals/search"
        payload = {"filterGroups":[{
             "filters":
                  [{"propertyName":"dealname",
                  "operator":"EQ",
                  "value":name}]
                  }],
              "sorts":[],
              "query":"",
              "properties":["name"],
              "limit":10,
              "after":0
              }
        response = requests.request("POST", url, json=payload, headers=self.headers, params=self.params)
        return response.json()   

    def create_contact(self, contact):
        url = "https://api.hubapi.com/crm/v3/objects/contacts/"
        payload = {"properties":{
                      "email":contact["EMAIL"],
                      "firstname":contact["FIRSTNAME"],
                      "lastname":contact["LASTNAME"],
                      "jobtitle":contact["JOB_TITLE"]
                  }
                }
        response = requests.request("POST", url, json=payload, headers=self.headers, params=self.params)
        return response.json()

    def del_deal(self, deal):
        url = "https://api.hubapi.com/crm/v3/objects/deals/{deal}"
        url = url.format(deal=deal)
        requests.delete(url, params=self.params)
       
    def create_deal(self, deal, pipe_line, stage):
        url = "https://api.hubapi.com/crm/v3/objects/deals/"
        payload = {"properties":{
                      "dealname":deal["DEAL"].strip(),
                      "pipeline":pipe_line,
                      "dealstage":stage
                  }
                }
        
        if "CLOSED_DATE" in deal and deal["CLOSED_DATE"]:
            payload["properties"]["closedate"] =  str(int(deal["CLOSED_DATE"].timestamp()))+"000"
        response = requests.request("POST", url, json=payload, headers=self.headers, params=self.params)
        return response.json()

    def add_association(self, from_obj, to, associations_type):
        if associations_type == 3:
            url = "https://api.hubapi.com/crm/v3/objects/deals/{from_obj}/associations/contact/{to}/{associations_type}"
            url = url.format(from_obj=from_obj, to=to, associations_type=associations_type)
        else:
            url = "https://api.hubapi.com/crm/v3/objects/deals/{from_obj}/associations/company/{to}/{associations_type}"
            url = url.format(from_obj=from_obj, to=to, associations_type=associations_type)
        response = requests.put(url, params=self.params)
        
        return response
    def get_pipe_line(self,name, stage_name):
        if self.pipelines:
            data = self.pipelines
        else:
            url = "https://api.hubapi.com/crm/v3/pipelines/deal"
            response = requests.get( url, params=self.params)
            data = response.json()
            self.pipelines = data
        for row in data["results"]:
            if row["label"].strip() == name.strip():
                for stage in row["stages"]:
                    if stage["label"].strip() ==  stage_name.strip():
                        return row["id"] ,stage["id"]
                
                
  
def delete(token, excel, name=False):
    try:
        if name:
            df = pd.read_excel(excel, sheet_name=name)
        else:
            df = pd.read_excel(excel, sheet_name=name)
    except:
        print("cant import excel file. stopping the script ")
        return 
    df = df.rename(columns=lambda x: x.strip())
    data = df.to_dict(orient="records")
    hub_obj = HubSpotDeal(token)
    for row in data:
        print("deleting ", row["DEAL"])
        deal = hub_obj.get_deal_by_name(row["DEAL"])
        for k in deal["results"]:
            hub_obj.del_deal(k["id"])

def connect(token, excel, name=False):
    try:
        
        if name:
            df = pd.read_excel(excel, sheet_name=name)
        else:
            df = pd.read_excel(excel, sheet_name=name)
    except:
        print("cant import excel file. stopping the script ")
        return 
    df = df.rename(columns=lambda x: x.strip())
    data = df.to_dict(orient="records")
    hub_obj = HubSpotDeal(token)
    for row in data:
        time.sleep(1)
        print("creating ", row["EMAIL"])
        pipe_line, stage = hub_obj.get_pipe_line(row["PIPELINE"], row["DEAL_STAGE"])
        time.sleep(1)
        company = hub_obj.get_company_by_name(row["COMPANY"])
        time.sleep(1)
        contact = hub_obj.get_contact_by_email(row["EMAIL"])

        if len(contact["results"]) == 0:
            res = hub_obj.create_contact(row)
            time.sleep(1)
            contact_id = res["id"]
        else:
            contact_id = contact["results"][0]['id']
        deal = hub_obj.get_deal_by_name(row["DEAL"])
        time.sleep(1)
        if len(deal["results"]) == 0:
            res = hub_obj.create_deal(row, pipe_line, stage)
            deal_id = res["id"]
        else:
            deal_id = deal["results"][0]["id"]
        time.sleep(1)
        hub_obj.add_association(deal_id,contact_id,3)
        if len(company["results"])> 1:
            hub_obj.add_association(deal_id,company["results"][0]["id"],5) 
        

if __name__ == '__main__':
    token = "e683ee2d-6a58-4cbe-b87c-2d0832bd26e0"
    excel = "Deal+contact_creation.xlsx"
    name = "Feuil1"
    to = delete(token, excel)
    to = connect(token, excel)
    
