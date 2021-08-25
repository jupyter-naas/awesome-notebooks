def extract_property(raw_property):
    # TODO: not handling files, formula, rollup and other complex property object
    property_type = raw_property["type"]

    if property_type == "date":
        if raw_property["date"]["end"]:
            return f'{raw_property["date"]["start"]} -> {raw_property["date"]["end"]}'
        return raw_property["date"]["start"]

    elif property_type in ["title", "rich_text"]:
        texts = [text["plain_text"] for text in raw_property[property_type]]
        return ",".join(texts)

    elif property_type == "select":
        return raw_property["select"]["name"]

    elif property_type == "multi_select":
        selections = [select["name"] for select in raw_property[property_type]]
        return ", ".join(selections)

    elif property_type in ["number", "url", "phone_number", "email", "checkbox"]:
        return raw_property[property_type]

    elif property_type == "people":
        return ", ".join([people["name"] for people in raw_property[property_type]])

    else:
        print(property_type, "is not implemented")
        return "Not implemented "


def insert_property(raw_property, value):
    # TODO: add people
    property_type = raw_property["type"]

    if property_type == "date":
        if isinstance(value, list) and len(value) == 2:
            raw_property["date"]["start"] = value[0]
            raw_property["date"]["end"] = value[1]
        elif isinstance(value, str):
            raw_property["date"]["start"] = value
            raw_property["date"]["end"] = None
        else:
            raise TypeError(
                "Date must be a '2021-08-28' or ['2021-08-28', '2021-10-28']"
            )

    if property_type in ["title", "rich_text"]:
        if isinstance(value, str):
            del raw_property[property_type][1:]
            raw_property[property_type][0]["plain_text"] = value
            raw_property[property_type][0]["text"]["content"] = value
        else:
            raise TypeError(f"{property_type} must be a string")

    if property_type == "select":
        if isinstance(value, str):
            raw_property[property_type] = {"name": value}
        else:
            raise TypeError(f"{property_type} must be a string")

    if property_type == "multi_select":
        if isinstance(value, str):
            raw_property[property_type].clear()
            raw_property[property_type] = [{"name": value}]
        elif isinstance(value, list):
            raw_property[property_type].clear()
            for elm in value:
                raw_property[property_type].append({"name": elm})
        else:
            raise TypeError(f"{property_type} must be a string or a list of string")

    elif property_type == "number":
        if isinstance(value, int):
            raw_property[property_type] = value
        else:
            raise TypeError(f"{property_type} must be an integer")

    elif property_type in ["url", "phone_number", "email"]:
        if isinstance(value, str):
            raw_property[property_type] = value
        else:
            raise TypeError(f"{property_type} must be a string or a list of string")
