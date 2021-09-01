from pandas.core.frame import DataFrame
import requests
import pandas as pd
import json
from helper import PropertyObject, BlockObject, PageObject
from helper import (
    unstack_properties,
)

# Notion version
_VERSION = "2021-08-16"

# TODO:
#   1. _repr_html_ -> with Page and content
#   2. find a way to update the content of a page
#   3. Work on the dockstring


class Connect:
    def __init__(self, token_api):
        self.token_api = token_api
        global _HEADERS
        _HEADERS = self.header
        self.test()

    @property
    def header(self):
        return {
            "Authorization": f"Bearer {self.token_api}",
            "Notion-Version": f"{_VERSION}",
            "Content-Type": "application/json",
        }

    def test(self):
        pass


class PageProperties(PageObject):
    def __init__(self, page_id) -> None:
        self.id = page_id
        page_object = self.retreive_properties()
        super().__init__(page_object)

    def retreive_properties(self) -> PageObject:
        request_url = f"https://api.notion.com/v1/pages/{self.id}"
        res = requests.get(request_url, headers=_HEADERS)
        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            return e
        return res.json()

    def update(self):
        url = f"https://api.notion.com/v1/pages/{self.id}"
        data = json.dumps({"properties": self.raw_properties})
        response = requests.patch(url, headers=_HEADERS, data=data)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e

        print("✨ Properties have been updated")


class PageContent:
    """Retrieves the content of a page using the ID specified."""

    def __init__(self, page_id) -> None:
        self.id = page_id
        self._blocks = self.retreive()

    def retreive(self) -> list[BlockObject]:
        url = f"https://api.notion.com/v1/blocks/{self.id}/children"
        response = requests.get(url, headers=_HEADERS)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        return [BlockObject(block) for block in response.json()["results"]]

    @property
    def content(self) -> pd.DataFrame:
        content = [block.get() for block in self._blocks]
        return pd.DataFrame(content)


class Page(PageProperties, PageContent):
    """The Page object contains the property values and the content of a single Notion Page."""

    def __init__(self, page_url) -> None:
        self.url = page_url
        self.id = page_url.split("-")[-1]

        PageProperties.__init__(self, self.id)
        PageContent.__init__(self, self.id)

    def _repr_html_(self):
        pass

    def update(self):
        PageProperties.update(self)
        self.refresh()

    def refresh(self):
        return self.__init__(self.url)

    def delete(self):
        pass

    def create(self):
        pass

    def duplicate(self):
        new_page = json.dumps(self.template)
        url = "https://api.notion.com/v1/pages"
        response = requests.post(url, headers=_HEADERS, data=new_page)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        print("✅ Your data was added to Notion")


class Database:
    """Database object contains page has childrens"""

    def __init__(self, page_url) -> None:
        self.url = page_url

        self._pages = self.retreive()
        # self.pages = self.clean_pages()

    @property
    def id(self):
        path = self.url.split("/")[-1]
        id = path.split("?")[0]
        return id

    def retreive(self):
        url = f"https://api.notion.com/v1/databases/{self.id}/query"
        response = requests.post(url, headers=_HEADERS)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        return [PageObject(page) for page in response.json()["results"]]

    def clean_pages(self) -> DataFrame:
        df = pd.DataFrame(self._raw_pages)
        df = unstack_properties(df)
        return df.applymap(extract_property)


if __name__ == "__main__":

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"

    Connect(TOKEN_API)
    page = Page(PAGE_URL)
    # page.content

    # DATABASE_URL = "https://www.notion.so/d0bb915c4cb4422a87679f3bb9658282?v=8cd7c6ea0ec244da9eb65aa88a87aabb"
    # database = Database(DATABASE_URL)
