from bs4 import BeautifulSoup
import requests

"""
class event, used to organize data for the events taking place at ucf
"""


class Events:
    def __init__(self):
        self.day = []
        self.start_time = []
        self.date = []
        self.link_storage = []
        self.name = []
        self.link = []


"""
Used to scrape the day catagory
"""


def ScrapeDay():
    url = "https://events.ucf.edu/"
    ucf_event = Events()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        """
        grabs all the links
        """
        for link in soup.findAll("a"):
            data = "".join(str(i) for i in link.get("href")).replace(
                "/event/", "https://events.ucf.edu/event/"
            )
            ucf_event.link_storage.append(link.get("href"))
            ucf_event.link.append(data)
        """
        grabs the names of events
        """
        for title in soup.findAll("h3"):
            data = (
                "".join(str(i) for i in title)
                .replace('<h3 class="event-title">', "")
                .replace('<a class="summary"', "")
                .replace("href=", "")
                .replace("</a>", "")
                .replace('"', "")
                .replace("<i class=fa fa-refresh></i>", "")
                .replace("<span class=sr-only>", "")
                .replace("</span>", "")
                .replace(">", "")
                .replace("\t", "")
            )
            ucf_event.name.append(data)
        """
        does some sorting to make it easier to read
        """
        ucf_event.link = ucf_event.link[19:29]
        ucf_event.link_storage = ucf_event.link_storage[19:29]
        ucf_event.name = ucf_event.name[0:5]
        """
        getting rid of some links we don't need in names
        """
        for i in range(len(ucf_event.link_storage)):
            ucf_event.name = [
                w.replace(ucf_event.link_storage[i], "") for w in ucf_event.name
            ]
        """
        grabbing the date we start this
        """
        for date in soup.findAll("span", attrs="start-date"):
            data = (
                "".join(str(i) for i in date)
                .replace('<span class="start-date">', "")
                .replace("</span>", "")
            )
            ucf_event.date.append(data)

        for time in soup.findAll("span", attrs="start-time"):
            data = (
                "".join(str(i) for i in time)
                .replace('<span class="start-time">', "")
                .replace("</span>", "")
            )
        return ucf_event
    except:
        print("No events")


"""
scrapes the data for that week and puts it into lists
"""


def scrape_weekly():
    url = "https://events.ucf.edu/this-week/"
    event_link = "https://events.ucf.edu/"
    ucf_event = Events()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    """
    grabs all the links
    """
    for link in soup.findAll("a"):
        data = "".join(str(i) for i in link.get("href")).replace(
            "/event/", "https://events.ucf.edu/event/"
        )
        ucf_event.link_storage.append(link.get("href"))
        ucf_event.link.append(data)
    """
    grabs the names of events
    """
    for title in soup.findAll("h3"):
        data = (
            "".join(str(i) for i in title)
            .replace('<h3 class="event-title">', "")
            .replace('<a class="summary"', "")
            .replace("href=", "")
            .replace("</a>", "")
            .replace('"', "")
            .replace("<i class=fa fa-refresh></i>", "")
            .replace("<span class=sr-only>", "")
            .replace("</span>", "")
            .replace(">", "")
            .replace("\t", "")
        )
        ucf_event.name.append(data)
    """
    does some sorting to make it easier to read, and remove duplicates
    """
    ucf_event.link = list(dict.fromkeys(ucf_event.link[19:69]))
    ucf_event.link_storage = list(dict.fromkeys(ucf_event.link_storage[19:69]))
    ucf_event.name = ucf_event.name[0:25]
    """
    getting rid of some links we don't need in names
    """
    for i in range(len(ucf_event.link_storage)):
        ucf_event.name = [
            w.replace(ucf_event.link_storage[i], "") for w in ucf_event.name
        ]
    """
    grabbing the date we start this
    """
    for date in soup.findAll("span", attrs="start-date"):
        data = (
            "".join(str(i) for i in date)
            .replace('<span class="start-date">', "")
            .replace("</span>", "")
        )
        ucf_event.date.append(data)
    """
    grabbing the time for the event
    """
    for time in soup.findAll("span", attrs="start-time"):
        data = (
            "".join(str(i) for i in time)
            .replace('<span class="start-time">', "")
            .replace("</span>", "")
        )
        ucf_event.start_time.append(data)
    return ucf_event
