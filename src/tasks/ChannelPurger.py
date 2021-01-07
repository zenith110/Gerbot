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
Checks the classes channels and determines if the channel is inactive/unused past a period of time and deletes
"""


async def ChannelPurger(bot: discord.ext.commands.bot.Bot):
    """
    Gets the current server so we can look at the channels
    """
    guild = bot.guilds[0]
    print(bot.guilds)
    print(guild)
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
    
    for channel_names in range(0, len(class_list)):
        """
        If there are no channels left, escape
        """
        try:
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
                date_of_creation = class_data[channel_names].created_at
                date_of_creation = date_of_creation.replace(
                    tzinfo=timezone.utc
                ).astimezone(tz=None)
                now = datetime.now()
                now = pytz.utc.localize(now)
                time_stamp = convert_date(time_stamp)
                now = convert_date(now)
                days_passed = abs(now - time_stamp)
                days = days_passed.days
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
                        classes_inactive_no_deleted.append(class_list[channel_names])
                        classes_inactive_no_deleted_days.append(days)
                    except:
                        break
                else:
                    days_remaining = abs(30 - days)
                    classes_inactive_no_messages.append(class_list[channel_names])
                    classes_inactive_no_days_left.append(days)
                    classes_inactive_no_days_remaining.append(days_remaining)
                    continue
        except:
            break
    """
    Assemble the json
    """
    data = {}
    inactive_message_json = []
    inactive_message_json_deleted = []
    inactive_no_message_json = []
    inactive_no_message_json_deleted = []
    inactive_json_data = {}
    inactive_json_data["inactive_messages"] = []
    inactive_json_deleted = {}
    inactive_json_deleted["inactive_messages_deleted"] = []
    inactive_no_json_data = {}
    inactive_no_json_data["inactive_no_messages"] = []
    inactive_no_deleted = {}
    inactive_no_deleted["inactive_no_messages_deleted"] = []

    for i in range(len(classes_inactive_messages)):
        inactive_json_data["inactive_messages"].append(
            {
                "name": classes_inactive_messages[i],
                "last_message_sent": str(classes_inactive_messages_days[i])
                + " days ago",
                "days_left_till_deletion": str(
                    classes_inactive_messages_days_remaining[i]
                )
                + " days left",
            }
        )
        inactive_message_json.append(inactive_json_data)
    for i in range(len(classes_inactive_deleted)):
        inactive_json_deleted["inactive_messages_deleted"].append(
            {
                "name": classes_inactive_messages[i],
                "total days": str(classes_inactive_messages_deleted_days[i])
                + " total days",
            }
        )
        inactive_message_json_deleted.append(inactive_json_deleted)

    for i in range(len(classes_inactive_no_messages)):
        inactive_no_json_data["inactive_no_messages"].append(
            {
                "name": classes_inactive_no_messages[i],
                "last_message_sent": str(classes_inactive_no_days_left[i])
                + " days ago",
                "days_left_till_deletion": str(classes_inactive_no_days_remaining[i])
                + " days left",
            }
        )
        inactive_no_message_json.append(inactive_no_json_data)
    for i in range(len(classes_inactive_no_deleted)):
        inactive_no_deleted["inactive_no_messages_deleted"].append(
            {
                "name": classes_inactive_no_deleted[i],
                "total days": str(classes_inactive_no_deleted_days[i]) + " total days",
            }
        )
        inactive_no_deleted.append(inactive_json_deleted)

    data["inactive_message"] = inactive_json_data
    data["inactive_message_deleted"] = inactive_message_json_deleted
    data["inactive_no_message"] = inactive_no_message_json
    data["inactive_no_deleted"] = inactive_no_deleted

    """
    Write the json file and send it to the channel
    """
    with open("classes_status.json", "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
    await channel_updates.send(file=discord.File("classes_status.json"))
