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


class RetreivePage:
    """Retrieves a Page object using the ID specified."""

    def __init__(self, page_id) -> None:
        self._page = RetreivePage.retreive(page_id)

    def __getitem__(self, key):
        return PropertyObject(self._page.properties[key]).extract()

    def __setitem__(self, key, value):
        return PropertyObject(self._page.properties[key]).insert(value)

    @staticmethod
    def retreive(page_id) -> PageObject:
        request_url = f"https://api.notion.com/v1/pages/{page_id}"
        res = requests.get(request_url, headers=_HEADERS)
        try:
            res.raise_for_status()
        except requests.HTTPError as e:
            return e
        return PageObject(res.json())

    @property
    def properties(self) -> pd.Series:
        data = {key: self[key] for key in self._page.properties.keys()}
        return pd.Series(data)

    @property
    def parent(self) -> dict:
        parent_object = self._page.parent
        parent_type = parent_object["type"]
        return {parent_type: parent_object[parent_type]}

    def update(self):
        url = f"https://api.notion.com/v1/pages/{self.id}"
        data = json.dumps({"properties": self._page.properties})
        response = requests.patch(url, headers=_HEADERS, data=data)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e

        print("✨ Properties have been updated")

    # def _refresh(self):
    #     self.__init__(self._page.id)


class RetreiveBlocks:
    """Retrieves the content of a page using the ID specified."""

    def __init__(self, page_id) -> None:
        self._blocks = RetreiveBlocks.retreive(page_id)

    @staticmethod
    def retreive(page_id) -> list[BlockObject]:
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        response = requests.get(url, headers=_HEADERS)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        return [BlockObject(block) for block in response.json()["results"]]

    @property
    def content(self) -> pd.DataFrame:
        content = [block.extract() for block in self._blocks]
        return pd.DataFrame(content)


class Page(RetreivePage, RetreiveBlocks):
    """The Page object contains the property values and the content of a single Notion Page."""

    # TODO:
    #   1. _repr_html_ -> with Page and content
    #   3. find a way to update the content of a page

    def __init__(self, page_url) -> None:
        self.url = page_url
        self.id = page_url.split("-")[-1]

        RetreivePage.__init__(self, self.id)
        RetreiveBlocks.__init__(self, self.id)

    def _repr_html_(self):
        pass

    def __repr__(self) -> str:
        pass

    def update(self):
        RetreivePage.update(self)

    # def _refresh(self):
    #     return super()._refresh()

    def delete(self):
        pass

    def create(self):
        pass

    @property
    def template(self):
        page_template = self._data_properties_properties.copy()

        for useless_key in [
            "object",
            "id",
            "created_time",
            "last_edited_time",
            "url",
            "archived",
        ]:
            page_template.pop(useless_key)
        page_template["parent"].pop("type")
        return page_template

    def duplicate(self):
        new_page = json.dumps(self._meta_properties)
        url = "https://api.notion.com/v1/pages"
        response = requests.post(url, headers=_HEADERS, data=new_page)
        return response
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        print("✅ Your data was added to Notion")


class Database:
    """ """

    def __init__(self, page_url) -> None:
        self.url = page_url

        self._raw_pages = self._retreive()
        self.pages = self._clean_pages()

    @property
    def id(self):
        path = self.url.split("/")[-1]
        id = path.split("?")[0]
        return id

    def _retreive(self):
        url = f"https://api.notion.com/v1/databases/{self.id}/query"
        response = requests.post(url, headers=_HEADERS)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            return e
        return response.json()["results"]

    def _clean_pages(self) -> DataFrame:
        df = pd.DataFrame(self._raw_pages)
        df = unstack_properties(df)
        return df.applymap(extract_property)


if __name__ == "__main__":

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"
    DATABASE_URL = "https://www.notion.so/d0bb915c4cb4422a87679f3bb9658282?v=8cd7c6ea0ec244da9eb65aa88a87aabb"

    Connect(TOKEN_API)
    page = Page(PAGE_URL)
