import json
import requests
from api_keys.cat import api_key
import random

"""
@arg - argument passed in by user
returns - string of image
"""


def ReturnCat(arg: str):
    url = "https://api.thecatapi.com/v1/images/search?breed_ids=" + arg
    response = requests.get(url, headers={"x-api-key": api_key}).json()
    for i in response:
        final_result = i["url"]
    return final_result


"""
Returns all cat breeds
"""


def ReturnAll():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, headers={"x-api-key": api_key}).json()
    names = []
    for i in response:
        names.append(i["id"])
    final_names = ", ".join(names)
    return final_names


def RandomCat():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, headers={"x-api-key": api_key}).json()
    names = []
    final_result = []
    for i in response:
        names.append(i["id"])
    final_name = random.choice(names)
    name_url = "https://api.thecatapi.com/v1/images/search?breed_ids=" + final_name
    name_response = requests.get(name_url, headers={"x-api-key": api_key}).json()
    final_result.append(final_name)
    for i in name_response:
        final_result.append(i["url"])
    return final_result
