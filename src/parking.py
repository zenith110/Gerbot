import requests                 # Used to make web requests
from bs4 import BeautifulSoup   # IO on html data
import os.path                  # Checks if file exists
import csv                      # CSV IO
from datetime import datetime   # Self explainatory
import pandas                   # Parses CSV output files on the disk

outputFile = 'garageData.csv' # output file global
url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx' # website where we're getting the data


def getGarageSite():
    """Helper function that requests and returns the UCF Parking Garage website source code"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def getMaxSpots(soup):
    """Returns array containing the max spots for every parking garage"""

    max_spots = []
    for length in soup.find_all("strong"):
        x = length.next_sibling.strip()
        x = x.strip('/')
        max_spots.append(int(x))
    return max_spots 


def getSpotsLeft(soup):
    """Returns array containing the total spots left for every parking garage"""

    current_spots = []
    for length in soup.find_all("strong"):
        x = int (length.get_text())
        current_spots.append(x)
    return current_spots

def getGarageNames(soup):
    """Returns array containing the name of each garage field"""

    garageNames = []
    for length in soup.find_all('td',{'class':'dxgv'}, text=True):
        x = length.get_text()
        garageNames.append(x)
    return  garageNames


def createDictionary(soup):
    """ Returns a dictionary with the Garage Name, Min Spots, and Max Spots"""

    x = dict(zip(getGarageNames(soup), zip(getSpotsLeft(soup), getMaxSpots(soup))))
    x.update(DateTime = datetime.now())
    return(x)
    

def garageStats():
    """Prints a hardcoded table to STDOUT containing all the parking garages and their respective data"""

    soup = getGarageSite()
    maxSpots = getMaxSpots(soup)
    spotsLeft = getSpotsLeft(soup)
    names = getGarageNames(soup)
    for i in range(len(names)):
        print(f"{names[i]}    : {spotsLeft[i]} / {maxSpots[i]} | {maxSpots[i] - spotsLeft[i]} Spots Taken ~ {100 - (spotsLeft[i]/maxSpots[i] * 100): .0f}% Full")


def exportCSV(soup):
    """ Exports the createDictionary function with an appended DateTime column into a CSV for parsing"""
    
    # Dynamically gets the headers of our csv file (the garage names)
    fieldnames = getGarageNames(soup)
    fieldnames.append("DateTime")
    dictionary = createDictionary(soup)

    # If the file exists, append the data rather than overwriting it
    if os.path.isfile(outputFile):
        with open(outputFile, mode='a') as exportFile:
            dataWriter = csv.DictWriter(exportFile, fieldnames=fieldnames)
            dataWriter.writerow(dictionary)
            return
    
    # If the file doesn't exist, create it and add the column headers
    else:
        with open(outputFile, mode='w') as exportFile:
            dataWriter = csv.DictWriter(exportFile, fieldnames=fieldnames)
            dataWriter.writeheader()
            dataWriter.writerow(dictionary)
            



def importCSV():
    """Outputs a formated csv file in table format"""

    # This is so easy it should be cheating
    df = pandas.read_csv(outputFile)
    print(df)



# def main():
#     # Get the website source code, extremely important (note it makes a web request every function call)
#     soup = getGarageSite()
    
#     # Create a data file; if it exists already it'll append the the csv sheet
#     # exportCSV(soup)

#     # Imports csv data file on the disk and outputs it to STDOUT
#     # importCSV()
    
#     # Outputs parking information to the terminal WITHOUT writing to disk
#     garageStats()


# if __name__ == "__main__":
#     main()