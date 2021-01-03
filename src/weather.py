import requests
from pprint import pprint

"""
class Weather, initialized with a list of 3 empty fields.
The name of the city, city's temperature, and the weather
description.
"""


class Weather:
    def __init__(self):
        self.name = ""
        self.temperature = ""
        self.description = ""


"""
Used to create and return a weather forecast 
"""


def GetForecast(arg: str):
    """
    Create a weather object.
    """
    forecast = Weather()

    """
    Access weather api
    """
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + arg
        + "&appid=842901232dd35d5226f8e52f0d6fed1e&units=imperial"
    )
    res = requests.get(url)

    data = res.json()

    """
    Fill in the fields in the weather object with data from the api
    """
    forecast.name = data["name"]
    forecast.temperature = str(data["main"]["temp"]) + "°"
    forecast.description = data["weather"][0]["description"]

    return forecast
