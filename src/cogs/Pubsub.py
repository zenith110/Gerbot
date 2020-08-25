import pubsub
import discord
from discord.ext import commands
from datetime import datetime
class Pubsub(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None









def setup(bot):
    bot.add_cog(Pubsub(bot))