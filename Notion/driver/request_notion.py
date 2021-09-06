import requests

VERSION = "2021-08-16"


def catch_error(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit("❌ Error:", err, response.text)


class RequestNotionAPI:
    URL: str
    id: str
    token: str

    def __init__(self, id, token) -> None:
        self.id = id
        self.token = token

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": f"{VERSION}",
            "Content-Type": "application/json",
        }


class RequestPage(RequestNotionAPI):
    URL = "https://api.notion.com/v1/pages/"

    def retreive(self):
        url = self.URL + self.id
        response = requests.get(url, headers=self.headers)
        catch_error(response)
        return response.json()

    def update(self, data):
        url = self.URL + self.id
        response = requests.patch(url, headers=self.headers, data=data)
        catch_error(response)
        print("✨ Properties have been updated")

    def create(self, data):
        url = self.URL
        response = requests.post(url, headers=self.headers, data=data)
        catch_error(response)
        print("✅ Page has been created")


class RequestBlock(RequestNotionAPI):
    URL = "https://api.notion.com/v1/blocks/"

    def retreive_children(self):
        url = self.URL + self.id + "/children"
        response = requests.get(url, headers=self.headers)
        catch_error(response)
        return response.json()["results"]
