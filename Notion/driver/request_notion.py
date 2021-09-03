import requests


def catch_error(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit("❌ Error:", err, response.text)


class RequestPage:
    URL = "https://api.notion.com/v1/pages/"

    def __init__(self, page_id, headers) -> None:
        self.id = page_id
        self.headers = headers

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


class RequestBlock:
    URL = "https://api.notion.com/v1/blocks/"

    def __init__(self, page_id, headers) -> None:
        self.id = page_id
        self.headers = headers

    def retreive_children(self):
        url = self.URL + self.id + "/children"
        response = requests.get(url, headers=self.headers)
        catch_error(response)
        return response.json()["results"]
