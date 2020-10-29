import requests
import smtplib
import pandas as pd
import markdown2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class HubSpot(object):
    """docstring for HubSpot"""
    def __init__(self, token):
        self.token = token
        self.deal_url = "https://api.hubapi.com/crm/v3/objects/deals/{deal}/"
        self.contacts_url = "https://api.hubapi.com/crm/v3/objects/contacts/{contact}"
    
    def get_contacts(self, deal):
        data_contact = []
        deal_url = self.deal_url.format(deal=deal)
        data = requests.get(deal_url, params={"associations":"contacts", "hapikey":self.token})
        deals = data.json()
        contacts = deals['associations']["contacts"]["results"]
        for contact in contacts:
            contacts_url = self.contacts_url.format(contact=contact["id"])
            data = requests.get(contacts_url, params={"properties":"hs_lead_status,email,jobtitle,firstname,lastname,company", "hapikey":self.token})
            contact_data = data.json()['properties']
            row = {}
            row["email"] = contact_data["email"]
            row["firstname"] = contact_data["firstname"]
            row["lastname"] = contact_data["lastname"]
            row["jobtitle"] = contact_data["jobtitle"]
            row["company"] = contact_data["company"]
            row["lead_status"] = contact_data["hs_lead_status"]
            data_contact.append(row)

        return data_contact
        

class sendEmail():
    def __init__(self, username, password, service = "gmail"):
        if service == "gmail":
            host ="smtp.gmail.com"
        elif service == "sendgrid":
            host = "smtp.sendgrid.net"
        self.conn = smtplib.SMTP(host,587)
        self.conn.starttls()
        self.conn.login(username,password)
    def send(self,to,subject,markdown, from_email,row):
        from_mail = from_email if from_email else self.username
        data = open(markdown).read()
        row["jobtitle"]  = row["jobtitle"] if row["jobtitle"] else ""
        row["company"]  = row["company"] if row["company"] else ""
        row["firstname"]  = row["firstname"] if row["firstname"] else ""
        data = data.replace("{firstname}",row["firstname"])
        data = data.replace("{company}",row["company"])
        data = data.replace("{jobtitle}",row["jobtitle"])
        html = markdown2.markdown(data)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to
        part = MIMEText(html, 'html')
        msg.attach(part)
        self.conn.sendmail(from_mail, to, msg.as_string())
        


def connect(token, deal):
    hub_obj = HubSpot(token)
    data  = hub_obj.get_contacts(deal)
    return pd.DataFrame(data)

def send_email(username, password, from_email, to,subject, markdown_path, service):
    mail = sendEmail(username, password, service)
    mail.send(to, subject, markdown_path,from_email)

def send_email_from_df(username,password,from_email,to_df,subject, markdown_path, service):
    mail = sendEmail(username, password, service)
    data = to_df.to_dict(orient="records")
    for row in data:
        print("sending to "+ row["email"])
        mail.send(row["email"], subject, markdown_path,from_email, row)
    mail.conn.close()

if __name__ == '__main__':
    token = "e683ee2d-6a58-4cbe-b87c-2d0832bd26e0"
    deal = "1992662234"
    to = connect(token, deal)
    print(to)


