import pandas as pd
import requests
import os
from typing import Dict
        
_VERSION = '2021-08-16'

def _extract_property(property_object):
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

class Notion:
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

class BlockObject(dict):
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""

    def __init__(self, dictionary) -> None:
        super().__init__(dictionary)
        self.object = dictionary.get("object")
        self.id = dictionary.get("id")
        self.type = dictionary.get("type")
        self.created_time = dictionary.get("created_time")
        self.last_edited_time = dictionary.get("last_edited_time")
        self.has_children = dictionary.get("has_children")
        self.value = dictionary.get(self.type)

    def extract(self) -> Dict:
        if self.type == "unsupported":
            return "unsupported"
        elif self.type == "child_page":
            return self.value["title"]
        elif self.type in ["bookmark", "pdf", "video", "image", "embed"]:
            return self.value["url"]
        else:
            array_of_rich_text = self.value["text"]
            content = [rich_text["plain_text"] for rich_text in array_of_rich_text]
            return " ".join(content)

    def insert(self, value) -> None:
        if self.type == "unsupported":
            return
        elif self.type == "child_page":
            self.value["title"] = value
        elif self.type in ["bookmark", "embed"]:
            self.value["url"] = value
        else:
            del self.value["text"][1:]
            self.value["text"][0]["text"]["content"] = value
            self.value["text"][0]["plain_text"] = value
            
class PageProperties:
    def __init__(self, properties: Dict):
        self.raw = properties

    def __getitem__(self, key):
        return _extract_property(self.raw[key])

    def __setitem__(self, key, value):
        return _extract_property(self.raw[key])

    def get(self) -> pd.Series:
        data = {key: self[key] for key in self.raw.keys()}
        return pd.Series(data)

    def __repr__(self) -> str:
        return f"{self.get()}"


class PageContent:
    def __init__(self, blocks) -> None:
        self.raw = [block for block in blocks]

    def __getitem__(self, index):
        return BlockObject(self.raw[index]).extract()

    def __setitem__(self, index, value):
        return BlockObject(self.raw[index]).insert(value)

    def get(self) -> pd.DataFrame:
        result = []
        for block in self.raw:
            block = BlockObject(block)
            result.append(
                {
                    "type": block.type,
                    "content": block.extract(),
                    "id": block.id,
                }
            )
        return pd.DataFrame(result)

    def __repr__(self) -> str:
        return f"{self.get()}"

    def _repr_html_(self):
        return self.get().to_html()

    
class Page(Notion):
    def __init__(self, headers, page_url=None):
        Notion.__init__(self)
        self.headers = headers
        if page_url:
            self.id = page_url.split("-")[-1]
        else:
            self.id = None
            
        # Request Parent
        url = f"https://api.notion.com/v1/pages/{self.id}"
        res = requests.get(url, headers=self.headers) 
        self.properties = PageProperties(res.json())
        
        # Request Content
        url = f"https://api.notion.com/v1/blocks/{self.id}/children"
        res = requests.get(url, headers=self.headers)
        content_object = res.json().get("results")
        if content_object:
            self.content = PageContent(content_object)
        
    def create(self, parent_id, data):
        return "Not Implemented yet"
    
    def delete(self, url):
        return "Not Implemented yet"

    
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
        df = df.applymap(_extract_property).dropna(how='all')
        df.columns = df.columns.str.upper()
        return df
    
    def create(self, url):
        return "Not Implemented yet"