import discord
from discord.ext import commands, tasks
from datetime import datetime, timezone
import re
import pytz


class ChannelHistory(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """
    Where the command is executed
    @self = self argument needed for the function
    @context = how we'll send messages
    @class_code = Class Code
    return - nothing
    """

    @commands.command(aliases=["time"])
    @commands.has_permissions(manage_roles=True)
    async def channel_history(self, context):
        current_channel_id = str(context.message.channel.mention)
        current_channel_name = str(context.message.channel)
        current_channel_id = "".join(e for e in current_channel_id if e.isalnum())
        messages = await context.channel.history(limit=1).flatten()
        time_stamp = messages[0].created_at
        time_stamp = time_stamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
        now = datetime.now()
        now = pytz.utc.localize(now)
        days_passed = now - time_stamp
        days = days_passed.days
        if days > 15:
            print("15 days have passed, let's remove!")
        else:
            print("Let's wait")


def setup(bot):
    bot.add_cog(ChannelHistory(bot))
