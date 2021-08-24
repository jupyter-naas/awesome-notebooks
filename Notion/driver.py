import requests
import pandas as pd
import json
from pprint import pprint

# Notion version
_VERSION = '2021-08-16'


class Connect:
    def __init__(self, token_api):
        self.token_api = token_api
        global HEADERS
        HEADERS = self.create_header()
        self.test()

    def create_header(self):
        return {
            'Authorization': f'Bearer {self.token_api}',
            'Notion-Version': f'{_VERSION}',
            'Content-Type': 'application/json'
        }

    def test(self):
        print("There is no test for the moment")


def get_id_from_database_url(database_url):
    return database_url.split('-')[-1]


class PageProperties:
    def __init__(self, page_url):
        page_id = get_id_from_database_url(page_url)
        url = f'https://api.notion.com/v1/pages/{page_id}'
        res = requests.get(url, headers=HEADERS)
        print(res)


class PageCreation:
    pass


class PageDuplication:
    pass


if __name__ == '__main__':
    TOKEN_API = 'secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq'
    PAGE_URL = 'https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86'

    Connect(TOKEN_API)
    PageProperties(PAGE_URL)
