import discord
import requests
from discord.ext import commands
import json


class Professor_Scraper(commands.Cog):
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
    deletes the role that is selected
    @self - self obj
    @context - how we'll send messages
    @prof_name - Professor name that will be searched
    @class_code - Code used to select 5 reviews
    return - nothing
    """

    @commands.command(pass_context=True, aliases=["class-review"])
    async def get_professor_rating(self, prof_name, class_code):
        command_prefix = "!class-review"
        command_name = "professor review"
        alias = "class-review"
        example = "!class-review matthew-gerber cop3502, unfinished"


def setup(bot):
    bot.add_cog(Professor_Scraper(bot))
