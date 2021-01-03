import academicCalendar
import discord
from discord.ext import commands
from disputils import BotEmbedPaginator

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

    @commands.command(aliases=["calendar", "academicCalendar", "ucfCalendar"])
    async def getCalendar(self, context):
        prod_mode = False
        command_prefix = "!calendar"
        command_name = "ucf academic calendar"
        alias = "calendar"
        example = "!calendar"
        """
        Create calendar object with strings containing the information to the
        calendar.
        """
        calendar = academicCalendar.makeCalendar()
        embeds = [
            discord.Embed(
                title="UCF Fall 2020 Academic Calendar",
                description=calendar.strings[0],
                inline=True,
                color=0x115599,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
            discord.Embed(
                title="UCF Fall 2020 Academic Calendar",
                description=calendar.strings[1],
                inline=True,
                color=0x5599FF,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
            discord.Embed(
                title="UCF Fall 2020 Academic Calendar",
                description=calendar.strings[2],
                inline=True,
                color=0x5599FF,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
            discord.Embed(
                title="UCF Fall 2020 Academic Calendar",
                description=calendar.strings[3],
                inline=True,
                color=0x5599FF,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
        ]
        paginator = BotEmbedPaginator(context, embeds)
        await paginator.run()


def setup(bot):
    bot.add_cog(Calendar(bot))
