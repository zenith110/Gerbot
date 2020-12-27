import datetime
from discord import utils
import pytz
import re
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


class ChannelPurge(commands.Cog):
    """
    Creates the instance of admin including its fields
    @bot - the bot itself
    @last_member - last member to use this
    return - nothing
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """  
    Deletes all classes in category
    @self - self obj
    @message - the message being scanned by the function
    return - nothing
    """

    @commands.command()
    @commands.has_role("Admin")
    async def purge(self, ctx):
        guild = ctx.guild
        class_list = []
        """
        Loops through all the channels using the regex for roles
        and appends them to a list
        """
        for channels in guild.text_channels:
            if re.search(r"\w+\d{4}c?-+\w", channels.name):
                class_list.append(channels.name)
        """
        Loops through all the classes list, and removes the channel and roles associated with them
        """
        for i in class_list:
            existing_channel = utils.get(guild.channels, name=i)
            role = utils.get(ctx.message.guild.roles, name=i)
            await role.delete()
            await existing_channel.delete()


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(ChannelPurge(bot))
