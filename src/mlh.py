import requests 
from bs4 import BeautifulSoup
import re
class mlh_events():
    def __init__(self):
        self.names = []
        self.beginning_dates = []
        self.locations = []
        self.links = []
        self.dates = []
        self.cities = []
        self.states = []
    def get_names(self):
        for names in self.names:
            print(names)

    def get_dates(self):
        for dates in self.dates:
            print(dates)

    def get_locations(self):
        for location in locations:
            print(location)

def parse_state(soup, mlh, states):
    for state in soup.findAll("span", itemprop="state"):
        data = ''.join(str(i) for i in state).replace('<span itemprop="state">', "").replace("</span>", "")
        states.append(data)
    mlh.states.append(states)

def parse_city(soup, mlh, cities):
    for city in soup.findAll("span", itemprop="city"):
        data = ''.join(str(i) for i in city).replace('<span itemprop="city">', "").replace("</span>", "")
        cities.append(data)
    mlh.cities.append(cities)

def parse_dates(soup, mlh, dates):
    for date in soup.findAll("p"):
        data = ''.join(str(i) for i in date).replace('<p class="event-date">', "").replace("Find, compete, and earn points for your school at the largest, most diverse student hackathons in the world.", "").replace("Major League Hacking © 2020", "")
        dates.append(data)
    mlh.dates.append(dates[1:])

def parse_link(soup, mlh, links):
    for link in soup.findAll("a"):
        links.append(link.get('href'))
    mlh.links.append(links[23:173])
    # print(mlh.links[0])

def parse_name(soup, events_names, mlh):
    for event_name in soup.findAll("h3"):
        # Replace all the stuff we don't need
        data = ''.join(str(i) for i in event_name).replace('<h3 class="event-name" itemprop="name"', "").replace("</h3>", "").replace(">", "").replace("\t", "").replace('<span class="__cf_email__', "").replace('" data-cfemail=', "").replace('e4ac85878fa4a7a1b3adb0341d1f173c3f392b3528d3faf8f0dbd8deccd2cf91b8bab2999a9c8e908d98b1b3bb9093958799846a220b09012a292f3d233e', "").replace('7f371e1c143f3c3a28362b"[email\xa0protected]</span', "").replace("c78fa6a4ac878482908e93", "").replace("703811131b303335273924", "").replace("[email\xa0protected]</span", "").replace("4f072e2c240f0c0a18061b", "").replace("246c45474f646761736d70", "").replace("f5bd94969eb5b6b0a2bca1", "").replace('"165e77757d565553415f42"', "")
        events_names.append(data)
    mlh.names.append(events_names[1:])

def parse_data(url):
    mlh = mlh_events()
    url = "https://mlh.io/seasons/na-2020/events"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []
    events_names = []
    dates = []
    cities = []
    states = []
    parse_name(soup, events_names, mlh)
    parse_link(soup, mlh, links)
    parse_dates(soup, mlh, dates)
    parse_city(soup, mlh, cities)
    parse_state(soup, mlh, states)
    return mlh
   

