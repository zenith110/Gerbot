import json
import requests
"""
@arg - argument passed in by user
returns - string of image
"""
def returnCat(arg):
    url = "https://api.thecatapi.com/v1/images/search?breed_ids=" + arg
    response = requests.get(url, headers={"x-api-key":"08b216cd-8951-4381-b1ec-ab05de908ae2"}).json()
    for i in response:
        final_result = i["url"]
    return final_result
"""
returns all cat breeds
"""
def returnAll():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, headers={"x-api-key":"08b216cd-8951-4381-b1ec-ab05de908ae2"}).json()
    names = []
    for i in response:
        names.append(i["id"])
    final_names = ", ".join(names)
    return final_names