import requests
from bs4 import BeautifulSoup
import os.path
from datetime import datetime

"""
Where we'll scrape the data from
"""
url = "https://secure.parking.ucf.edu/GarageCount/iframe.aspx"

"""
Helper function that requests and returns the UCF Parking Garage website source code
"""


def GetGarageSite():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


"""
Returns array containing the max spots for every parking garage
"""


def GetMaxSpots(soup: BeautifulSoup):

    max_spots = []
    for length in soup.find_all("strong"):
        x = length.next_sibling.strip()
        x = x.strip("/")
        max_spots.append(int(x))
    return max_spots


"""
Returns array containing the total spots left for every parking garage
"""


def GetSpotsLeft(soup: BeautifulSoup):

    current_spots = []
    for length in soup.find_all("strong"):
        x = int(length.get_text())
        current_spots.append(x)
    return current_spots


"""
Returns array containing the name of each garage field
"""


def GetGarageNames(soup: BeautifulSoup):

    garageNames = []
    for length in soup.find_all("td", {"class": "dxgv"}, text=True):
        x = length.get_text()
        garageNames.append(x)
    return garageNames


""" 
Returns a dictionary with the garage name, min spots, and max spots
"""


def CreateDictionary(soup: BeautifulSoup):

    x = dict(zip(GetGarageNames(soup), zip(GetSpotsLeft(soup), GetMaxSpots(soup))))
    x.update(DateTime=datetime.now())
    return x


"""
Prints a hardcoded table to STDOUT containing all the parking garages and their respective data
"""


def GarageStats():

    soup = GetGarageSite()
    max_spots = GetMaxSpots(soup)
    spots_left = GetSpotsLeft(soup)
    names = GetGarageNames(soup)
    for i in range(len(names)):
        print(
            f"{names[i]}    : {spots_left[i]} / {max_spots[i]} | {max_spots[i] - spots_left[i]} Spots Taken ~ {100 - (spots_left[i]/max_spots[i] * 100): .0f}% Full"
        )
