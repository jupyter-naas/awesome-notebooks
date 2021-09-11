from abc import ABC, abstractmethod
from typing import Dict


class Block(ABC):
    def __init__(self, dictionary: Dict) -> None:
        self.object = dictionary.get("object")
        self.id = dictionary.get("id")
        self.type = dictionary.get("type")
        self.created_time = dictionary.get("created_time")
        self.last_edited_time = dictionary.get("last_edited_time")
        self.has_children = dictionary.get("has_children")
        self.value = dictionary.get(self.type)

    @abstractmethod
    def get(self):
        "Implemented in the subclass"

    @abstractmethod
    def set(self, value):
        "Implemented in the subclass"

    @abstractmethod
    def create(self, value):
        "Implemented in the subclass"


class ArrayOfRichText(Block):
    def get(self):
        content = [rich_text["plain_text"] for rich_text in self.value["text"]]
        return " ".join(content)

    def set(self, value: str):
        del self.value["text"][1:]
        self.value["text"][0]["text"]["content"] = value
        self.value["text"][0]["plain_text"] = value

    @staticmethod
    def create(text: str, link: str = None):
        return {"text": [{"type": "text", "text": {"content": text, "link": link}}]}


class Heading1(ArrayOfRichText):
    @staticmethod
    def create(text: str, link: str = None):
        return {"type": "heading_1", "heading_1": ArrayOfRichText.create(text, link)}


class Heading2(ArrayOfRichText):
    @staticmethod
    def create(text: str, link: str = None):
        return {"type": "heading_2", "heading_2": ArrayOfRichText.create(text, link)}


class Heading3(ArrayOfRichText):
    @staticmethod
    def create(text: str, link: str = None):
        return {"type": "heading_3", "heading_3": ArrayOfRichText.create(text, link)}


class Embed(Block):
    def get(self):
        return self.value["url"]

    def set(self, value):
        self.value["url"] = value

    @staticmethod
    def create(text: str, link: str = None):
        return {"type": "embed", "embed": {"url": "https://website.domain"}}
