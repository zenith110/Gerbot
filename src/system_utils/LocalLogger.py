import traceback
import datetime
import pytz

"""
Prints the call stack to the console
"""


def LocalLogger():
    now = datetime.datetime.now(pytz.timezone("America/New_York"))
    if now.hour > 12:
        hour = now.hour - 12
        message = (
            str(now.month)
            + "/"
            + str(now.day)
            + "/"
            + str(now.year)
            + " - "
            + str(hour)
            + ":"
            + str(now.minute)
            + " PM \n"
            + traceback.format_exc()
        )
        print(message)
    else:
        hour = now.hour - 12
        message = (
            str(now.month)
            + "/"
            + str(now.day)
            + "/"
            + str(now.year)
            + " - "
            + str(hour)
            + ":"
            + str(now.minute)
            + " AM \n"
            + traceback.format_exc()
        )
        print(message)
