import requests
import random

"""
@comic_num - argument passed in by user
returns - json data for xkcd comic
"""
def getComic(comic_num):
    url = f"https://xkcd.com/{comic_num}/info.0.json"
    res = requests.get(url)
    j = res.json()

    return j

def getRandomComic():
    url = f"https://xkcd.com/info.0.json"
    res = requests.get(url)
    j = res.json()
    num = j["num"]

    comic_num = random.randint(0, num)

    url = f"https://xkcd.com/{comic_num}/info.0.json"
    res = requests.get(url)
    j = res.json()

    return j

def getTodayComic():
    url = f"https://xkcd.com/info.0.json"
    res = requests.get(url)
    j = res.json()

    return j