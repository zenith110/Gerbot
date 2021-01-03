import datetime
import discord
import pytz
from discord.ext import commands


class Report(commands.Cog):
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
    Sends a report to the      
    @self - self obj
    @message - the message being scanned by the function
    return - nothing
    """

    @commands.command(aliases=["report"])
    async def Report(self, context: discord.ext.commands.context.Context, *args: list):
        command_prefix = "!report"
        command_name = "report"
        alias = "report"
        example = "!report <anonymous report message>"
        """
        Setup the channel where the reports will be sent to
        """
        report_channel = self.bot.get_channel(751495912299430020)

        """  
        Setup the report message
        """
        msg = " ".join(args)

        """  
        Setup the timezone information
        """
        est = pytz.timezone("US/Eastern")

        """  
        Checks if the report is being sent via DM, if so send to report channel
        """
        if (
            "Direct Message with" in str(context.channel)
            and context.author != self.bot.user
        ):
            embed = discord.Embed(
                title="Report", timestamp=datetime.datetime.now(tz=est)
            )
            embed.add_field(name="Anonymous Report", value=msg, inline=True)
            await report_channel.send(embed=embed)


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Report(bot))
