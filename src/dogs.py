import json
import requests
"""
fetches name
@arg - argument passed by user
returns - image
"""
def returnDog(arg):
    url = "https://dog.ceo/api/breed/" + arg + "/images/random" 
    response = requests.get(url).json()
    image = response["message"]
    print(image)
    return image
"""
fetches all breeds
returns - name
"""
def returnAll():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url).json()
    names = []
    for i in response["message"]:
        names.append(i)
    final_names = ", ".join(names)
    return final_names