import mlh
import discord
from discord.ext import commands
from datetime import datetime
"""
MLH command
"""
class MLH(commands.Cog):
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
    return - nothing
    """
    @commands.command(aliases = ['mlh'])
    async def getMlh(self, context):
        """
        Fetches the current the current MLH events till October 2020
        """
        url = "https://mlh.io/seasons/2021/events"
        mlh_obj = mlh.parse_data(url)
        mlh_message = discord.Embed(title="MLH events", description="Current MLH events for the 2020 year")
        for i in range(0, 17):
            mlh_message.add_field(name=str(mlh_obj.dates[0][i]), value="[" + str(mlh_obj.names[0][i]) + "](" + str(mlh_obj.links[0][i]) + ")\n" + str(mlh_obj.cities[0][i]) + ", " + str(mlh_obj.states[0][i]), inline=True)
        await context.send(embed=mlh_message)

    @commands.command(aliases = ['currentMlh'])
    async def getCurrentMlh(self, context):
        url = "https://mlh.io/seasons/2021/events"
        mlh_obj = mlh.get_relevent_date(url)
        month = datetime.now().month
        year = datetime.now().year
        day = datetime.now().day
        full = datetime(year, month, day)
        mlh_message = discord.Embed(title=full.strftime("%b") + " " + str(year) + " hackathons", description="Current MLH events coming up this month")
        for i in range(0, len(mlh_obj.current_month_events)):
            mlh_message.add_field(name=full.strftime("%b"), value=mlh_obj.current_month_events[i], inline=True)
        await context.send(embed=mlh_message)


def setup(bot):
    bot.add_cog(MLH(bot))