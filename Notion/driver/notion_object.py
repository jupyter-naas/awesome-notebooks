import pandas as pd


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


class PageProperties:
    def __init__(self, raw_properties) -> None:
        self.raw = raw_properties

    def __getitem__(self, key):
        raw_property = PropertyObject(self.raw[key])
        return raw_property.extract()

    def __setitem__(self, key, value):
        raw_property = PropertyObject(self.raw[key])
        return raw_property.insert(value)

    def get(self) -> pd.Series:
        data = {key: self[key] for key in self.raw.keys()}
        return pd.Series(data)

    def __repr__(self) -> str:
        return f"{self.get()}"


class PageObject:
    """The Page object contains the property values of a single Notion page."""

    def __init__(self, page_object: dict) -> None:
        self.raw = page_object
        self.object = page_object["object"]
        self.id = page_object["id"]
        self.created_time = page_object["created_time"]
        self.last_edited_time = page_object["last_edited_time"]
        self.archived = page_object["archived"]
        self.icon = page_object["icon"]
        self.cover = page_object["cover"]
        self.properties = PageProperties(page_object["properties"])
        self.parent = page_object["parent"]
        self.url = page_object["url"]

        self.title = self.properties["Name"]


class BlockObject:
    """A block object represents content within Notion. Blocks can be text, lists, media, and more. A page is a type of block, too!."""

    def __init__(self, block_object) -> None:
        self.raw = block_object
        self.object = block_object["object"]
        self.id = block_object["id"]
        self.type = block_object["type"]
        self.created_time = block_object["created_time"]
        self.last_edited_time = block_object["last_edited_time"]
        self.has_children = block_object["has_children"]
        self.value = block_object[self.type]

    def extract(self):
        if self.type == "child_page":
            return self.value["title"]
        else:
            array_of_rich_text = self.value["text"]
            content = [rich_text["plain_text"] for rich_text in array_of_rich_text]
            return " ".join(content)

    def insert(self, value):
        if self.type == "child_page":
            self.value["title"] = value
        else:
            del self.value["text"][1:]
            self.value["text"][0]["text"]["content"] = value
            self.value["text"][0]["plain_text"] = value


class PageContent:
    def __init__(self, blocks: list) -> None:
        self.raw = [BlockObject(block) for block in blocks]

    def __getitem__(self, index):
        return self.raw[index].extract()

    def get(self) -> pd.DataFrame:
        result = []
        for block in self.raw:
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


class TemplateObject:
    def __init__(self, page_object: PageObject, content_object: PageContent) -> None:
        self.page_object = page_object

        self.parent = self.page_object["parent"].copy()
        self.parent.pop("type")

        self.content_object = content_object.copy()
        self.children = [
            block.raw for block in self.content_object  # if block.type != "child_page"
        ]

    def create(self):
        return {
            "parent": self.parent,
            "properties": self.page_object["properties"],
            "children": self.children,
            "icon": self.page_object["icon"],
            "cover": self.page_object["cover"],
        }
