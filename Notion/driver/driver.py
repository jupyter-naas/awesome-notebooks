import json
from notion_object import (
    PageObject,
    PageContent,
    TemplateObject,
)
from request_notion import RequestPage, RequestBlock


class Page(PageObject):
    page_url: str
    token_api: str

    def __init__(self, page_url, token_api) -> None:
        self.token_api = token_api
        self.url = page_url
        self.id = page_url.split("-")[-1]

        page_object = RequestPage(self.id, token_api).retreive()
        super().__init__(page_object)

        page_content = RequestBlock(self.id, token_api).retreive_children()
        self.content = PageContent(page_content)

    def update(self):
        data = json.dumps(self.raw)
        RequestPage(self.id, self.token_api).update(data)

    def refresh(self):
        return self.__init__(self.url)

    def duplicate(self):
        template = TemplateObject(self, self.content.raw, self.token_api).create()
        new_page = json.dumps(template)
        RequestPage(self.id, self.token_api).create(new_page)


if __name__ == "__main__":

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"

    page = Page(PAGE_URL, TOKEN_API)
    # page.properties["Email"] = "axelito@gmail.com"
    page.properties["Completion Time"] = 4
