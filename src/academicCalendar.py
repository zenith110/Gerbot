import bs4 
import requests

"""
class academicCalendar, initialized with a list of 4 empty strings.
These strings will hold the contents of the academic calendar.
"""
class academicCalendar():
    def __init__(self):
        self.strings = ['','','','']

"""
Used to scrape the UCF academic calendar.
"""
def makeCalendar():
    """
    Create calendar object.
    """
    calendar = academicCalendar()

    url = 'https://calendar.ucf.edu/2020/fall'
    res = requests.get(url)
    res.raise_for_status()

    calendarSoup = bs4.BeautifulSoup(res.content, 'html.parser')

    """
    Select all of the summaries for the events. 
    """
    summaries = calendarSoup.select('.summary')

    """
    Select all of the dates to the events. 
    """
    dates = calendarSoup.select('.dtstart')

    """
    Index used to keep track on which string in the calendar object we are on.
    """
    index = 0

    """
    Store the event summaries and dates in the strings in the calendar object.
    """
    for i in range(len(summaries)):
        summary = summaries[i].getText()
        date = dates[i].getText()
        
        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary. 
        """
        if summary == 'For Undergraduate International Students':
            calendar.strings[index] += '\n__**Application Deadlines**__\n'
        
            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + '\n__**Application Deadlines**__\n') >= 1024:
                index = index + 1

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary. 
        """
        if summary == 'Enrollment Appointment Date and Time Available for Fall 2020 on myUCF':
            calendar.strings[index] += '\n__**Academic Dates and Deadlines**__\n'
            
            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + '\n__**Academic Dates and Deadlines**__\n') >= 1024:
                index = index + 1
            

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary.
        """
        if summary == 'Labor Day':
            calendar.strings[index] += '\n__**Holidays**__\n'

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + '\n__**Holidays**__\n') >= 1024:
                index = index + 1

        """
        If the event summary we are looking at equals this we need to add 
        this header before storing the summary.
        """
        if summary == 'Homecoming Week':
            calendar.strings[index] += '\n__**Special Events**__\n'

            """
            Discord embeds can only hold strings that are 1024 chars or less.
            So if adding this text will make the string over 1024 chars,
            we move on to the next string in the calendar object.
            """
            if len(calendar.strings[index] + '\n__**Special Events**__\n') >= 1024:
                index = index + 1

        """
        Discord embeds can only hold strings that are 1024 chars or less.
        So if adding this summary will make the string over 1024 chars,
        we move on to the next string in the calendar object.
        """
        if len(calendar.strings[index] + summary + '\n' + date + '\n') >= 1024:
                index = index + 1

        """
        Store the event summary in the string in the calendar object
        """
        calendar.strings[index] += summary + '\n' + date + '\n\n'

    return calendar
