import mlh
import discord
from discord.ext import commands
"""
MLH command that s
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
    @commands.command()
    async def getMlh(self, context):
        url = "https://mlh.io/seasons/na-2020/events"
        mlh_obj = mlh.parse_data(url)
        mlh_message = discord.Embed(title="MLH events till October", description="Current MLH events for the 2020 year")
        for i in range(0, 32):
            mlh_message.add_field(name=str(mlh_obj.dates[0][i]), value="[" + str(mlh_obj.names[0][i]) + "](" + str(mlh_obj.links[0][i]) + ")\n" + str(mlh_obj.cities[0][i]) + ", " + str(mlh_obj.states[0][i]), inline=True)
        await context.send(embed=mlh_message)
        


def setup(bot):
    bot.add_cog(MLH(bot))