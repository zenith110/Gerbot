import academicCalendar
import discord
from discord.ext import commands

"""
Academic Calendar command.
"""
class Calendar(commands.Cog):
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
    async def getCalendar(self, context):
        """
        Create calendar object with strings containing the information to the
        calendar.
        """
        calendar = academicCalendar.makeCalendar()

        """
        Create discord embeds
        """
        embed1 = discord.Embed(title = 'UCF Fall 2020 Academic Calendar')
        embed2 = discord.Embed(title = 'UCF Fall 2020 Academic Calendar')
        embed3 = discord.Embed(title = 'UCF Fall 2020 Academic Calendar')
        embed4 = discord.Embed(title = 'UCF Fall 2020 Academic Calendar')

        """
        Add the information to the discord embeds
        """
        embed1.add_field(name = '1/4', value = calendar.strings[0], inline = True)
        embed2.add_field(name = '2/4',value = calendar.strings[1], inline = True)
        embed3.add_field(name = '3/4',value = calendar.strings[2], inline = True)
        embed4.add_field(name = '4/4',value = calendar.strings[3], inline = True)

        """
        Send the discord embeds
        """
        await context.send(embed = embed1)
        await context.send(embed = embed2)
        await context.send(embed = embed3)
        await context.send(embed = embed4)

def setup(bot):
    bot.add_cog(Calendar(bot))

    
