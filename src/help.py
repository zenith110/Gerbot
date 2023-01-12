import json


def PageData(commands_link: json, start: int, end: int):
    data = []
    for i in range(start, end):
        names = ", ".join(commands_link[i]["name"])
        data.append(
            "**"
            + commands_link[i]["name"]
            + "**"
            + "\nCommand Prefix: "
            + commands_link[i]["command-prefix"]
            + "\n"
        )

    value_string = "\n".join(data)
    return value_string
