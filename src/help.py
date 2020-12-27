import json


def page_data(commands_link: json, start: int, end: int):
    data = []
    for i in range(start, end):
        names = ", ".join(commands_link[i]["names"])
        sub_arguments = ", ".join(commands_link[i]["sub-commands"])

        data.append(
            "**"
            + commands_link[i]["name"]
            + "** - "
            + commands_link[i]["example"]
            + "\n"
            + commands_link[i]["description"]
            + "\n"
            + "Aliases: ["
            + names
            + "]"
            + "\nSub Arguments: ["
            + sub_arguments
            + "]\n"
        )

    value_string = "\n".join(data)
    return value_string
