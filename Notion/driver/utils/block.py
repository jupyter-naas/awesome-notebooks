from typing import Dict
from blocks import *

mapping = {
    "heading_1": Heading1,
    "heading_2": Heading2,
    "heading_3": Heading3,
    "embed": Embed,
}


def extract_block(block_object):
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""
    block_type = block_object.get("type")
    return mapping[block_type](block_object).get()


def insert_block(block_object, value):
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""
    block_type = block_object.get("type")
    return mapping[block_type](block_object).set(value)

    # def extract(self) -> Dict:
    #     if self.type == "unsupported":
    #         return "unsupported"
    #     elif self.type == "child_page":
    #         return self.value["title"]
    #     elif self.type in ["bookmark", "pdf", "video", "image", "embed"]:
    #         return self.value["url"]
    #     else:
    #         array_of_rich_text = self.value["text"]
    #         content = [rich_text["plain_text"] for rich_text in array_of_rich_text]
    #         return " ".join(content)

    # def insert(self, value) -> None:
    #     if self.type == "unsupported":
    #         return
    #     elif self.type == "child_page":
    #         self.value["title"] = value
    #     elif self.type in ["bookmark", "embed"]:
    #         self.value["url"] = value
    #     else:
    #         del self.value["text"][1:]
    #         self.value["text"][0]["text"]["content"] = value
    #         self.value["text"][0]["plain_text"] = value


if __name__ == "__main__":
    block_example = {
        "type": "heading_1",
        "heading_1": {
            "text": [
                {
                    "type": "text",
                    "text": {"content": "I am a Heading 1", "link": None},
                    "plain_text": "I am a Heading 1",
                    "href": None,
                }
            ]
        },
    }
    # block.insert("hello")
    # print(block.extract())
