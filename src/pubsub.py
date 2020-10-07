"""
Fetches the latest pub sub deal 
"""
import requests
class randomsub():
    def __init__(self):
        self.innards = None
        self.sub_name = ""
        self.last_sale = ""
        self.on_sale = ""
        self.price = ""
        self.image = ""
def get_pub_sub(sub_name):
    sub_name = sub_name.replace(" ", "-")
    url = "https://pubsub-api.dev/subs/?name=" + sub_name
    response = requests.get(url).json()
    sub = randomsub()
    sub.sub_name = response[0]["sub_name"]
    sub.last_sale = response[0]["last_sale"]
    sub.status = response[0]["status"]
    sub.price = response[0]["price"]
    sub.image = response[0]["image"]
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