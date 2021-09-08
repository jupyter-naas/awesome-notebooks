import json
from lib.request import RequestPageProperties, RequestPage
from lib.page import PageObject


class Page(PageObject):
    def __init__(self, page_url, token_api) -> None:
        self.token_api = token_api
        self.url = page_url
        self.id = page_url.split("-")[-1]

        self._create_page()

    def _create_page(self):
        self.raw = RequestPage(self.id, self.token_api)
        super().__init__(**self.raw.retreive())

    def update(self):
        RequestPageProperties(self.id, self.token_api).update(self.raw.properties)
        for block in self.raw.content:
            RequestPageProperties(block["id"], self.token_api).update(block)

    def refresh(self):
        return self.__init__(self.url)

    # def duplicate(self):
    #     template = TemplateObject(self, self.content.raw, self.token_api).create()
    #     new_page = json.dumps(template)
    #     RequestPage(self.id, self.token_api).create(new_page)


if __name__ == "__main__":

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Bitcoin-aaca5f6afecc4bbfa29c8d2e17901e18"

    page = Page(PAGE_URL, TOKEN_API)
    # page.properties["Email"] = "axelito@gmail.com"
    # page.properties["Completion Time"] = 4
    # page.update()
