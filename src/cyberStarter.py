import json

"""
Gets the cyberstarter json file and returns the dumped data
"""


def getFile():
    with open("./cyberstarter.json") as f:
        data = json.load(f)

    return data
