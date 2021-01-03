import bs4
import requests

"""
class AcademicCalendar, initialized with a list of 4 empty strings.
These strings will hold the contents of the academic calendar.
"""


class AcademicCalendar:
    def __init__(self):
        self.strings = ["", "", "", ""]


"""
Used to scrape the UCF academic calendar.
"""


def MakeCalendar():
    """
    Create calendar object.
    """
    calendar = AcademicCalendar()

    url = "https://calendar.ucf.edu/2020/fall"
    res = requests.get(url)
    res.raise_for_status()

    calendar_soup = bs4.BeautifulSoup(res.content, "html.parser")

    """
    Select all of the events for the events. 
    """
    events = calendar_soup.select(".vevent")

    """
    Select all of the summaries for the events. 
    """
    summaries = calendar_soup.select(".summary")

    """
    Select all of the dates to the events. 
    """
    dates = calendar_soup.select(".dtstart")

    """
    Select all of the end dates to events that have one.
    """
    end_dates = calendar_soup.select(".dtend")

    """
    Index used to keep track on which string in the calendar object we are on.
    """
    index = 0

    """
    Index used to keep track of end dates for events with a date range.
    """
    end_date_index = 0

    """
    Store the event summaries and dates in the strings in the calendar object.
    """
    for i in range(len(events)):
        summary = summaries[i].getText()
        date = dates[i].getText()
        end_date = ""

        """
        If the event has a date range be sure to include the end date.
        """
        if "dtend" in str(events[i]):
            end_date = "  -  " + end_dates[end_date_index].getText()
            end_date_index = end_date_index + 1

        date = date + end_date

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary. 
        """
        if summary == "For Undergraduate International Students":
            calendar.strings[index] += "\n__**Application Deadlines**__\n"

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if (
                len(calendar.strings[index] + "\n__**Application Deadlines**__\n")
                >= 1024
            ):
                index = index + 1

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary. 
        """
        if (
            summary
            == "Enrollment Appointment Date and Time Available for Fall 2020 on myUCF"
        ):
            calendar.strings[index] += "\n__**Academic Dates and Deadlines**__\n"

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if (
                len(
                    calendar.strings[index] + "\n__**Academic Dates and Deadlines**__\n"
                )
                >= 1024
            ):
                index = index + 1

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary.
        """
        if summary == "Labor Day":
            calendar.strings[index] += "\n__**Holidays**__\n"

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + "\n__**Holidays**__\n") >= 1024:
                index = index + 1

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary.
        """
        if summary == "Homecoming Week":
            calendar.strings[index] += "\n__**Special Events**__\n"

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + "\n__**Special Events**__\n") >= 1024:
                index = index + 1

        """
        Discord embeds can only hold strings that are 1024 chars or less.
        So if adding this summary will make the string over 1024 chars,
        we move on to the next string in the calendar object.
        """
        if len(calendar.strings[index] + summary + "\n" + date + "\n") >= 1024:
            index = index + 1

        """
        Store the event summary in the string in the calendar object
        """
        calendar.strings[index] += summary + "\n" + date + "\n\n"

    return calendar
