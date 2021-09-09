import pandas as pd
import requests
import os
        
_VERSION = '2021-08-16'




# def insert(self, value):
#     if self.type == "date":
#         if isinstance(value, list) and len(value) == 2:
#             self.value["start"] = value[0]
#             self.value["end"] = value[1]
#         elif isinstance(value, str):
#             self.value["start"] = value
#             self.value["end"] = None
#         else:
#             raise TypeError(
#                 "Date must be a '2021-08-28' or ['2021-08-28', '2021-10-28']"
#             )

#     if self.type in ["title", "rich_text"]:
#         if isinstance(value, str):
#             del self.value[1:]
#             self.value[0]["plain_text"] = value
#             self.value[0]["text"]["content"] = value
#         else:
#             raise TypeError(f"{self.type} must be a string")

#     if self.type == "select":
#         if isinstance(value, str):
#             self.raw[self.type] = {"name": value}
#         else:
#             raise TypeError(f"{self.type} must be a string")

#     if self.type == "multi_select":
#         if isinstance(value, str):
#             self.raw[self.type].clear()
#             self.raw[self.type] = [{"name": value}]
#         elif isinstance(value, list):
#             self.raw[self.type].clear()
#             for elm in value:
#                 self.raw[self.type].append({"name": elm})
#         else:
#             raise TypeError(f"{self.type} must be a string or a list of string")

#     elif self.type == "number":
#         if isinstance(value, int):
#             self.raw[self.type] = value
#         else:
#             raise TypeError(f"{self.type} must be an integer")

#     elif self.type in ["url", "phone_number", "email"]:
#         if isinstance(value, str):
#             self.raw[self.type] = value
#         else:
#             raise TypeError(f"{self.type} must be a string or a list of string")


class Notion():
    
    def _extract_property(self, property_object):
        property_type = property_object["type"]
        property_value = property_object[property_type]

        if property_value is None:
            return None
        else:
            if property_type == "date":
                if property_value["end"]:
                    return f'{property_value["start"]} -> {property_value["end"]}'
                return property_value["start"]

            elif property_type in ["title", "rich_text"]:
                texts = [text["plain_text"] for text in property_value]
                return ",".join(texts)

            elif property_type == "select":
                return property_value["name"]

            elif property_type == "multi_select":
                selections = [select["name"] for select in property_value]
                return ", ".join(selections)

            elif property_type in ["number", "url", "phone_number", "email", "checkbox"]:
                return property_value

            elif property_type == "people":
                peoples = [
                    people.get("name") for people in property_value if people.get("name")
                ]
                return ", ".join(peoples)
        
    def connect(self, api_token):
        # Init thinkific attribute
        self.header = {'Authorization': f'Bearer {api_token}',
                       'Notion-Version': f'{_VERSION}',
                       'Content-Type': 'application/json'}

        # Init end point
        self.page = Page(self.header)
        self.database = Database(self.header)

        # Set connexion to active
        self.connected = True
        return self


class Page(Notion):
    def __init__(self, headers):
        Notion.__init__(self)
        self.headers = headers
        
#     def get_content(data):
#         return data
        
#     def get_properties(data):
#         return data
    
#     def create(self, parent_id, data):
#         data = {}
#         return parent_id
    
#     def get(self, url):
#         return url
    
#     def update(self, parent_id):
#         return parent_id
    
#     def delete(self, url):
#         return url

class Database(Notion):
    def __init__(self, headers):
        Notion.__init__(self)
        self.headers = headers
    
    def _get_id(self, url):
        path = url.split('/')[-1]
        uid = path.split('?')[0]
        return uid
    
    def get(self, url):
        uid = self._get_id(url)
        req_url = f'https://api.notion.com/v1/databases/{uid}/query'
        
        # Request
        res = requests.post(req_url,
                            headers=self.headers)
        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            return(e)

        # Get json
        res_json = res.json()

        # Parse json
        results = res_json.get("results")

        data = []
        for r in results:
            properties = r.get("properties")
            data.append(properties)

        df = pd.DataFrame(data)
        df = df.applymap(self._extract_property)
        df.columns = df.columns.str.upper()
        return df