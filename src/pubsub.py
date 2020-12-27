"""
Fetches the latest pub sub deal 
"""
import requests


class randomsub:
    def __init__(self):
        self.innards = None
        self.sub_name = ""
        self.last_sale = ""
        self.on_sale = ""
        self.price = ""
        self.image = ""
        self.status_code = ""


def get_all_subs():
    try:
        url = "https://pubsub-api.dev/allsubs/"
        response = requests.get(url).json()
        sub_names = []
        for i in range(len(response)):
            sub_names.append(response[i]["name"])
        subs = ", ".join(sub_names)
        return subs
    except:
        return "API is down..."


def get_pub_sub(sub_name):
    sub_name = sub_name.replace(" ", "-")
    url = "https://pubsub-api.dev/subs/?name=" + sub_name
    try:
        response = requests.get(url).json()
        sub = randomsub()
        sub.sub_name = response[0]["sub_name"]
        sub.last_sale = response[0]["last_sale"]
        sub.status = response[0]["status"]
        sub.price = response[0]["price"]
        sub.image = response[0]["image"]
        sub.status_code = "OK"
        return sub
    except:
        sub = randomsub()
        sub.status_code = "404"
        return sub


def empty_sub_input():
    sub = randomsub()
    url = "https://pubsub-api.dev/subs/?name="
    response = requests.get(url).json()

    sub.sub_name = response[0]["sub_name"]
    sub.last_sale = response[0]["last_sale"]
    sub.status = response[0]["status"]
    sub.price = response[0]["price"]
    sub.image = response[0]["image"]
    return sub
