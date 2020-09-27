"""
Fetches the latest pub sub deal 
"""
class randomsub():
    def __init__(self):
        self.innards = None
        self.sub_name = ""
        self.last_sale = ""
        self.on_sale = ""
        self.price = ""
        self.image = ""
import requests
def get_pub_sub(sub_name):
    sub_name = sub_name.replace(" ", "-")
    url = "https://pubsub-api.dev/subs/?name=" + sub_name
    response = requests.get(url).json()
    return response
def empty_sub_input():
    sub = randomsub()
    url = "https://pubsub-api.dev/subs/?name="
    response = requests.get(url).json()
    for x in response:
        sub.sub_name = response[x][0]["sub_name"]
        sub.last_sale = response[x][0]["last_sale"]
        sub.status = response[x][0]["status"]
        sub.price = response[x][0]["price"]
        sub.image = response[x][0]["image"]
    return sub