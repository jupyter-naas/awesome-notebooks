import requests
import pandas as pd
import json
from pprint import pprint
from helper import extract_property, insert_property

# Notion version
_VERSION = "2021-08-16"


def get_id_from_page_url(page_url):
    return page_url.split("-")[-1]


class Connect:
    def __init__(self, token_api):
        self.token_api = token_api
        global _HEADERS
        _HEADERS = self.create_header()
        self.test()

    def create_header(self):
        return {
            "Authorization": f"Bearer {self.token_api}",
            "Notion-Version": f"{_VERSION}",
            "Content-Type": "application/json",
        }

    def test(self):
        pass


class Page:
    def __init__(self, page_url):
        if page_url:
            self.id = get_id_from_page_url(page_url)

            raw_properties = self.request()

            self.properties = PageProperties(raw_properties)
            self.content = PageContent(self)

    def request(self):
        url = f"https://api.notion.com/v1/pages/{self.id}"
        res = requests.get(url, headers=_HEADERS)
        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            return e
        return res.json()

    def create(self, database_url):
        pass

    def update(self):
        pass


class PageProperties:
    def __init__(self, raw_properties):
        self.raw = raw_properties

        # self.archived = raw_properties["archived"]
        # self.icon = raw_properties["icon"]["emoji"]
        # self.cover = raw_properties["cover"]

    def __getitem__(self, key):
        raw_property = self.raw["properties"][key]
        return extract_property(raw_property)

    def __setitem__(self, key, value):
        raw_property = self.raw["properties"][key]
        return insert_property(raw_property, value)

    def show(self):
        data = {key: self[key] for key in self.raw["properties"].keys()}
        index = [f'{self.raw["icon"]["emoji"]}  {self["Name"]}']
        return pd.DataFrame(data=[data], index=index).T

    def update(self):
        # TODO: add a try catch and a validation message
        page_id = self.raw["id"]
        url = f"https://api.notion.com/v1/pages/{page_id}"
        data = json.dumps({"properties": self.raw["properties"]})
        response = requests.patch(url, headers=_HEADERS, data=data)
        try:
            response.raise_for_status()
            print("✨ Properties have been updated")
        except requests.HTTPError as e:
            return e


class PageContent:
    def __init__(self, page):
        pass


if __name__ == "__main__":
    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"

    Connect(TOKEN_API)
    page = Page(PAGE_URL)
