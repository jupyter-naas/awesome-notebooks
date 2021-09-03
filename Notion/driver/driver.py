import requests
import pandas as pd
import json
from notion_object import (
    PropertyObject,
    BlockObject,
    PageObject,
    PageContent,
    TemplateObject,
)
from request_notion import RequestPage, RequestBlock

VERSION = "2021-08-16"

# TODO:
#   1. _repr_html_ -> with Page and content
#   2. find a way to update the content of a page
#   3. Work on the dockstring


def connect(token_api):
    global HEADERS
    HEADERS = {
        "Authorization": f"Bearer {token_api}",
        "Notion-Version": f"{VERSION}",
        "Content-Type": "application/json",
    }


class Page(PageObject):
    def __init__(self, page_url) -> None:
        self.url = page_url
        self.id = page_url.split("-")[-1]

        page_object = RequestPage(self.id, HEADERS).retreive()
        super().__init__(page_object)

        page_content = RequestBlock(self.id, HEADERS).retreive_children()
        self.content = PageContent(page_content)

    def update(self):
        data = json.dumps(self.raw)
        RequestPage(self.id, HEADERS).update(data)

    def refresh(self):
        return self.__init__(self.url)

    def duplicate(self):
        template = TemplateObject(self.raw, self.content.raw).create()
        new_page = json.dumps(template)
        RequestPage(self.id, HEADERS).create(new_page)


if __name__ == "__main__":

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"

    connect(TOKEN_API)
    page = Page(PAGE_URL)
    page.duplicate()
