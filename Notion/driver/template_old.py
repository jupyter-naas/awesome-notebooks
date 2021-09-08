class TemplateObject:
    def __init__(self, page_object, content_object, headers) -> None:
        self.page_object = page_object.raw

        self.parent = self.page_object["parent"].copy()
        self.parent.pop("type")

        self.children = []
        for block in content_object:
            if block.type != "child_page":
                block.retreive_children(headers)
                self.children.append(block.raw)

    def create(self):
        return {
            "parent": self.parent,
            "properties": self.page_object["properties"],
            "children": self.children,
            "icon": self.page_object["icon"],
            "cover": self.page_object["cover"],
        }
