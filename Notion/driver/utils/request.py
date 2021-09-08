from dataclasses import dataclass
import requests
from typing import Dict
import json

VERSION = "2021-08-16"


def catch_error(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise Exception("❌ Error:", err, response.text)


@dataclass
class RequestNotionAPI:
    id: str
    token: str

    def __post_init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": f"{VERSION}",
            "Content-Type": "application/json",
        }


class RequestPageProperties(RequestNotionAPI):
    URL = "https://api.notion.com/v1/pages/"

    def retreive(self) -> Dict:
        url = self.URL + self.id
        response = requests.get(url, headers=self.headers)
        catch_error(response)
        return response.json()

    def update(self, data) -> None:
        url = self.URL + self.id
        data = json.dumps(data)
        response = requests.patch(url, headers=self.headers, data=data)
        catch_error(response)
        print("✨ Properties have been updated")

    def create(self, data) -> None:
        url = self.URL
        response = requests.post(url, headers=self.headers, data=data)
        catch_error(response)
        print("✅ Page has been created")


class RequestBlock(RequestNotionAPI):
    URL = "https://api.notion.com/v1/blocks/"

    def update(self, data):
        url = self.URL + self.id
        data = json.dumps(data)
        response = requests.patch(url, headers=self.headers, data=data)
        catch_error(response)
        print("✅ Block has been updated")


class RequestChildren(RequestNotionAPI):
    URL = "https://api.notion.com/v1/blocks/"

    def retreive(self) -> Dict:
        url = self.URL + self.id + "/children"
        response = requests.get(url, headers=self.headers)
        catch_error(response)
        return response.json()["results"]

    def append(self, data):
        url = self.URL + self.id + "/children"

        data = {"children": [data]}
        data = json.dumps(data)

        response = requests.patch(url, headers=self.headers, data=data)
        catch_error(response)
        print("✅ Block have been add to your page")


class RequestPage(RequestNotionAPI):
    def retreive(self) -> Dict:
        """Retreive all the page properties & childrens."""
        self.properties = RequestPageProperties(self.id, self.token).retreive()
        self.content = RequestChildren(self.id, self.token).retreive()
        return {**self.properties, "content": self.content}

    def update(self, data) -> None:
        RequestPageProperties(self.id, self.token).update(data)
