class Property:
    """An object describing by an id, type, and value of a page property."""

    def __init__(self, property_object) -> None:
        self.raw = property_object
        self.id = property_object["id"]
        self.type = property_object["type"]
        self.value = property_object[self.type]

    def extract(self):
        if self.value is None:
            return None
        else:
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
                self.raw[self.type] = {"name": value}
            else:
                raise TypeError(f"{self.type} must be a string")

        if self.type == "multi_select":
            if isinstance(value, str):
                self.raw[self.type].clear()
                self.raw[self.type] = [{"name": value}]
            elif isinstance(value, list):
                self.raw[self.type].clear()
                for elm in value:
                    self.raw[self.type].append({"name": elm})
            else:
                raise TypeError(f"{self.type} must be a string or a list of string")

        elif self.type == "number":
            if isinstance(value, int):
                self.raw[self.type] = value
            else:
                raise TypeError(f"{self.type} must be an integer")

        elif self.type in ["url", "phone_number", "email"]:
            if isinstance(value, str):
                self.raw[self.type] = value
            else:
                raise TypeError(f"{self.type} must be a string or a list of string")
