import json
import requests
"""
Strip it of the extra flutter that comes with lists
"""
def getName(arg):
    return arg
def returnDog(arg):
    url = "https://dog.ceo/api/breed/" + arg + "/images/random" 
    response = requests.get(url).json()
    return response