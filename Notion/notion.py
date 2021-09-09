# from naas_drivers.driver import InDriver, OutDriver
# from notion.client import NotionClient
import pandas as pd
import requests
import os


# class Notion(InDriver, OutDriver):
#     def __init__(self):
#         self.auth_proxy = os.getenv("NAAS_AUTH_PROXY")

#     def connect(
#         self,
#         token: str = None,
#         email: str = None,
#         password: str = None,
#     ):
#         if token:
#             self.client = NotionClient(token)
#         elif email and password:
#             self.client = NotionClient(token_v2=self.__token_v2(email, password))
#         else:
#             self.print_error("You should provide, token or email/pasword")
#         self.connected = True
#         return self

#     def __token_v2(
#         self,
#         email: str,
#         password: str,
#     ):
#         url = f"https://www.notion.so/login&filter=token_v2&email={email}&password={password}"
#         cookie_response = requests.get(f"{self.auth_proxy}/token?url={url}")
#         return cookie_response.json()["cookies"][0]["value"]

#     def get(self, url: str):
#         self.check_connect()
#         page = self.client.get_block(url)
#         return page

#     def get_collection(
#         self,
#         url: str,
#         raw: bool = False,
#     ):
#         self.check_connect()
#         cv = self.client.get_collection_view(url)
#         if raw:
#             return cv
#         else:
#             data = [
#                 block_row.get_all_properties() for block_row in cv.collection.get_rows()
#             ]
#             return pd.DataFrame(data)
        
_VERSION = '2021-08-16'


class Notion():
    
    def extract_text(self, dictionnary):
        if 'name' in dictionnary:
            return dictionnary['name']
        elif 'plain_text' in dictionnary:
            return dictionnary['plain_text']
        else:
            return ''

    def extract_date(self, dictionnary):
        '''
        For the moment we extract only the starting date of a date field
        Example {'id': 'prop_1', 'type': 'date', 'date': {'start': '2018-03-21', 'end': None}}
        '''
        return dictionnary['start']

    def extract_data(self, element):
        ''' 
        input: a dictionnary of a notion property
        Exemple: {'id': 'W#4k', 'type': 'select', 'select': {'id': 'b305bd26-****-****-****-c78e2034db8f', 'name': 'Client', 'color': 'green'}}
        output: the string containing the information of the dict. (Client in the exemple)
        '''
        if type(element) is dict:
            dict_type = element['type'] 
            informations = element[dict_type]

            if type(informations) is dict:
                if dict_type == 'date':
                    return self.extract_date(informations)
                else:
                    return self.extract_text(informations)

            elif type(informations) is list:
                informations = [self.extract_text(elm) for elm in informations]
                return ','.join(informations)
            else:
                return informations
        else:
            return ''
        
    def connect(self, api_token):
        # Init thinkific attribute
        self.header = {'Authorization': f'Bearer {api_token}',
                       'Notion-Version': f'{_VERSION}',
                       'Content-Type': 'application/json'}

        # Init end point
        self.page = Page(self.header)
        self.datebase = Database(self.header)

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
        
    def __get_database_id(self, url):
        path = url.split('/')[-1]
        uid = path.split('?')[0]
        return uid
    
    def get(self, url):
        # Get id from page
        uid = self.__get_database_id(url)
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
        df = df.applymap(self.extract_data).dropna()
        df.columns = df.columns.str.upper()
        return df

