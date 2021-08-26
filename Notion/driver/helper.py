class PropertyObject:
    """An object describing by an id, type, and value of a page property."""

    def __init__(self, property_object) -> None:
        self.id = property_object["id"]
        self.type = property_object["type"]
        self.value = property_object[self.type]

    def extract(self):
        if self.value:

            if self.type == "date":
                if self.value["end"]:
                    return f'{self.value["start"]} -> {self.value["end"]}'
                return self.value["start"]

            elif self.type in ["title", "rich_text"]:
                texts = [text["plain_text"] for text in self.value]
                return ",".join(texts)

            elif self.type == "select":
                return self.value["name"]

            elif self.type == "multi_select":
                selections = [select["name"] for select in self.value]
                return ", ".join(selections)

            elif self.type in ["number", "url", "phone_number", "email", "checkbox"]:
                return self.value

            elif self.type == "people":
                peoples = [
                    people.get("name") for people in self.value if people.get("name")
                ]
                return ", ".join(peoples)
        else:
            return None

    def insert(self, value):
        if self.type == "date":
            if isinstance(value, list) and len(value) == 2:
                self.value["start"] = value[0]
                self.value["end"] = value[1]
            elif isinstance(value, str):
                self.value["start"] = value
                self.value["end"] = None
            else:
                raise TypeError(
                    "Date must be a '2021-08-28' or ['2021-08-28', '2021-10-28']"
                )

        if self.type in ["title", "rich_text"]:
            if isinstance(value, str):
                del self.value[1:]
                self.value[0]["plain_text"] = value
                self.value[0]["text"]["content"] = value
            else:
                raise TypeError(f"{self.type} must be a string")

        if self.type == "select":
            if isinstance(value, str):
                self.value = {"name": value}
            else:
                raise TypeError(f"{self.type} must be a string")

        if self.type == "multi_select":
            if isinstance(value, str):
                self.value.clear()
                self.value = [{"name": value}]
            elif isinstance(value, list):
                self.value.clear()
                for elm in value:
                    self.value.append({"name": elm})
            else:
                raise TypeError(f"{self.type} must be a string or a list of string")

        elif self.type == "number":
            if isinstance(value, int):
                self.value = value
            else:
                raise TypeError(f"{self.type} must be an integer")

        elif self.type in ["url", "phone_number", "email"]:
            if isinstance(value, str):
                self.value = value
            else:
                raise TypeError(f"{self.type} must be a string or a list of string")


class PageObject:
    """The Page object contains the property values of a single Notion page."""

    def __init__(self, page_object) -> None:
        self.properties = page_object["properties"]
        self.parent = page_object["parent"]
        self.icon = page_object["icon"]
        self.cover = page_object["cover"]

        self.object = page_object["object"]
        self.id = page_object["id"]
        self.created_time = page_object["created_time"]
        self.last_edited_time = page_object["last_edited_time"]
        self.archived = page_object["archived"]
        self.url = page_object["url"]


class BlockObject:
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""

    def __init__(self, block_object) -> None:
        self.id = block_object["id"]
        self.type = block_object["type"]
        self.last_edited_time = block_object["last_edited_time"]
        self.created_time = block_object["created_time"]
        self.value = block_object[self.type]

    @property
    def content(self):
        if self.type == "child_page":
            return self.value["title"]
        else:
            array_of_rich_text = self.value["text"]
            content = [rich_text["plain_text"] for rich_text in array_of_rich_text]
            return " ".join(content)

    def extract(self):
        return {
            "type": self.type,
            "content": self.content,
            "id": self.id,
        }


def unstack_properties(df):
    import pandas as pd

    list_dict = [row["properties"] for _, row in df.iterrows()]
    return pd.DataFrame(list_dict)
