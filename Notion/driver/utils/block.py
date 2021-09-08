from typing import Dict


class BlockObject(dict):
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""

    def __init__(self, dictionary) -> None:
        super().__init__(dictionary)
        self.object = dictionary.get("object")
        self.id = dictionary.get("id")
        self.type = dictionary.get("type")
        self.created_time = dictionary.get("created_time")
        self.last_edited_time = dictionary.get("last_edited_time")
        self.has_children = dictionary.get("has_children")
        self.value = dictionary.get(self.type)

    def extract(self) -> Dict:
        if self.type == "unsupported":
            return "unsupported"
        elif self.type == "child_page":
            return self.value["title"]
        elif self.type in ["bookmark", "pdf", "video", "image", "embed"]:
            return self.value["url"]
        else:
            array_of_rich_text = self.value["text"]
            content = [rich_text["plain_text"] for rich_text in array_of_rich_text]
            return " ".join(content)

    def insert(self, value) -> None:
        if self.type == "unsupported":
            return
        elif self.type == "child_page":
            self.value["title"] = value
        elif self.type in ["bookmark", "embed"]:
            self.value["url"] = value
        else:
            del self.value["text"][1:]
            self.value["text"][0]["text"]["content"] = value
            self.value["text"][0]["plain_text"] = value


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
    block = BlockObject(block_example)
    block.insert("hello")
    print(block.extract())
