import json
import requests
import random

"""
fetches name
@arg - argument passed by user
returns - image
"""


def ReturnDog(arg: str):
    url = "https://dog.ceo/api/breed/" + arg + "/images/random"
    response = requests.get(url).json()
    image = response["message"]
    return image


"""
fetches all breeds
returns - name
"""


def ReturnAll():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url).json()
    names = []
    for i in response["message"]:
        names.append(i)
    final_names = ", ".join(names)
    return final_names


def ReturnRandomDog():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url).json()
    names = []
    final_result = []
    for i in response["message"]:
        names.append(i)
    final_names = random.choice(names)
    final_result.append(final_names)
    name_url = "https://dog.ceo/api/breed/" + final_names + "/images/random"
    response = requests.get(name_url).json()
    final_result.append(response["message"])
    return final_result
