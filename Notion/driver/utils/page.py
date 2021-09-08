from typing import Dict
import pandas as pd
from dataclasses import dataclass

from .property import Property
from .block import BlockObject


class PageProperties:
    def __init__(self, properties: Dict):
        self.raw = properties

    def __getitem__(self, key):
        return Property(self.raw[key]).extract()

    def __setitem__(self, key, value):
        return Property(self.raw[key]).insert(value)

    def get(self) -> pd.Series:
        data = {key: self[key] for key in self.raw.keys()}
        return pd.Series(data)

    def __repr__(self) -> str:
        return f"{self.get()}"


class PageContent(list):
    def __init__(self, blocks) -> None:
        self.raw = [block for block in blocks]

    def __getitem__(self, index):
        return BlockObject(self.raw[index]).extract()

    def __setitem__(self, index, value):
        return BlockObject(self.raw[index]).insert(value)

    def get(self) -> pd.DataFrame:
        result = []
        for block in self.raw:
            block = BlockObject(block)
            result.append(
                {
                    "type": block.type,
                    "content": block.extract(),
                    "id": block.id,
                }
            )
        return pd.DataFrame(result)

    def __repr__(self) -> str:
        return f"{self.get()}"

    def _repr_html_(self):
        return self.get().to_html()


@dataclass
class PageObject:
    object: str
    id: str
    created_time: str
    last_edited_time: str
    archived: bool
    icon: Dict
    cover: Dict
    properties: Dict
    parent: Dict
    url: str
    content: list

    def __post_init__(self):
        self.properties = PageProperties(self.properties)
        self.content = PageContent(self.content)


if __name__ == "__main__":

    from request import RequestPage

    TOKEN_API = "secret_R1CrUGn8bx9itbJW0Fc9Cc0R9Lmhbnz2ayqEe0GhRPq"
    PAGE_URL = "https://www.notion.so/Tom-Simon-2ccdafe28955478b8c9d70bda0044c86"

    PAGE_ID = PAGE_URL.split("-")[-1]
    page_object = RequestPage(PAGE_ID, TOKEN_API).retreive()
    page = PageObject(**page_object)
