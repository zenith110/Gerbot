"""
Fetches the latest pub sub deal 
"""
import requests
def get_pub_sub(sub_name):
    sub_name = sub_name.replace(" ", "-")
    url = "http://pubsub-api.dev/?name=" + sub_name
    response = requests.get(url).json()
    return response