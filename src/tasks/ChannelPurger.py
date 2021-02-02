import re
import pytz
from datetime import datetime, timezone
import discord
import json
import discord.utils

"""
Converts datetime objects to string and to datetime objects to determine date length
"""


def convert_date(date):
    date = date.strftime("%m/%d/%y")
    date = datetime.strptime(date, "%m/%d/%y")
    return date
"""
Given a list, loop through till you found the server and return the index
"""


def return_position_server(server_list: list, server_name: str):
    index = 0
    for i in range(0, len(server_list)):
        if(server_list[i].name == server_name):
            index = i
        else:
            continue
    return index
    
"""
Checks the classes channels and determines if the channel is inactive/unused past a period of time and deletes
"""

async def ChannelPurger(bot: discord.ext.commands.bot.Bot):
    """
    Gets the current server so we can look at the channels
    """
    server_index = return_position_server(bot.guilds, "UCF IT")
    guild = bot.guilds[server_index]

    """
    Will send the file to a specific channel on the server
    """
    channel_updates = bot.get_channel(795013556693237800)
    """
    Holds the various data that will create the json, and allows us to delete roles and classes
    """
    class_list = []
    class_data = []
    classes_inactive_messages_deleted = []
    classes_inactive_messages_deleted_days = []
    classes_inactive_deleted = []
    classes_inactive_messages = []
    classes_inactive_messages_days_remaining = []
    classes_inactive_messages_days = []
    classes_inactive = []
    classe_inactive_days = []
    classes_inactive_no_messages = []
    classes_inactive_no_days_left = []
    classes_inactive_no_days_remaining = []
    classes_inactive_no_deleted = []
    classes_inactive_no_deleted_days = []

    """
    Loops through all the channels using the regex for roles
    and appends them to a list
    """
    for channels in guild.text_channels:
        if re.search("([a-z][a-z][a-z]\d\d\d\d)", channels.name):
            class_list.append(channels.name)
            class_data.append(channels)
        else:
            continue
    """
    Loops through the class list and grabs the channels, and looks at time stamp to determine what to do with it
    """
    print(class_list)
    for channel_names in range(0, len(class_list)):
        """
        If there are no channels left, escape
        """
        try:
            print("Attempting to get a channel!")
            channel = discord.utils.get(
                guild.text_channels, name=class_list[channel_names]
            )
            """
            If there is content/messages, let's look into it
            """
            try:
                """
                Grabs the time stamp and our current date, and does magic to get home many days left till then
                """
                messages = await channel.history(limit=100).flatten()
                time_stamp = messages[0].created_at
                time_stamp = time_stamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
                now = datetime.now()

                now = pytz.utc.localize(now)
                time_stamp = convert_date(time_stamp)
                now = convert_date(now)

                days_passed = abs(now - time_stamp)
                days = days_passed.days
                """
                Deletes if over 30 days
                """
                if days > 30:
                    try:
                        existing_channel = discord.utils.get(
                            guild.channels, name=class_list[channel_names]
                        )
                        role = discord.utils.get(
                            guild.roles, name=class_list[channel_names]
                        )
                        await role.delete()
                        await existing_channel.delete()
                        classes_inactive_deleted.append(class_list[channel_names])
                        classes_inactive_messages_deleted_days.append(days)

                    except:
                        break

                else:
                    days_remaining = abs(30 - days)
                    classes_inactive_messages.append(class_list[channel_names])
                    classes_inactive_messages_days_remaining.append(days_remaining)
                    classes_inactive_messages_days.append(days)
                    continue

            except:
                print("Channel is brand new, let's look at when it was created!")
                date_of_creation = class_data[channel_names].created_at
                date_of_creation = date_of_creation.replace(
                    tzinfo=timezone.utc
                ).astimezone(tz=None)
                print(class_data[channel_names])
                now = datetime.now()
                now = pytz.utc.localize(now)
                
                time_stamp = convert_date(date_of_creation)
                print(time_stamp)
                
                now = convert_date(now)
                days_passed = abs(now - time_stamp)
                
                days = days_passed.days
                print(str(days) + " since this channel was created!")
                if days > 30:
                    try:
                        print("Channel is past 30 days!")
                        print("Let's clean up!")
                        existing_channel = discord.utils.get(
                            guild.channels, name=class_list[channel_names]
                        )
                        role = discord.utils.get(
                            guild.roles, name=class_list[channel_names]
                        )
                        await role.delete()
                        await existing_channel.delete()
                        classes_inactive_no_deleted.append(class_list[channel_names])
                        classes_inactive_no_deleted_days.append(days)
                    except:
                        print("Clean up could not be done!")
                        break
                else:
                    days_remaining = abs(30 - days)
                    classes_inactive_no_messages.append(class_list[channel_names])
                    classes_inactive_no_days_left.append(days)
                    classes_inactive_no_days_remaining.append(days_remaining)
                    continue
        except:
            break
    
   
    
