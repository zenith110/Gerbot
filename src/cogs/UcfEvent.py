import discord
from discord.ext import commands
from datetime import datetime
import ucf_events


class UcfEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["event", "ucfEvent", "getEvent"])
    async def GetUcfEvent(self, context, argument=None):
        """
        Allows us to get events happening at UCF. Uses day and weekly.
        """
        month = datetime.now().month
        year = datetime.now().year
        day = datetime.now().day
        full = datetime(year, month, day)
        if argument == None:
            await context.send("Please pass in day, or weekly for the calander")
        if argument == "day":
            ucf_day_event = ucf_events.ScrapeDay()
            event_message = discord.Embed(
                title="UCF events",
                description="Current events happening at UCF on "
                + full.strftime("%m/%d/%Y"),
            )
            try:
                for i in range(0, len(ucf_day_event.name)):
                    event_message.add_field(
                        name=str(ucf_day_event.date[i]),
                        value="["
                        + str(ucf_day_event.name[i])
                        + "]"
                        + "("
                        + str(ucf_day_event.link[i])
                        + ")",
                        inline=True,
                    )
                await context.send(embed=event_message)
            except:
                await context.send(
                    "No events are currently happening today, please refer to https://events.ucf.edu/event/ for the list"
                )

        elif argument == "weekly":
            ucf_day_event = ucf_events.ScrapeWeekly()
            event_message = discord.Embed(
                title="UCF events",
                description="Current events happening at UCF on the week of "
                + full.strftime("%m/%d/%Y"),
            )
            try:
                for i in range(0, len(ucf_day_event.name)):
                    event_message.add_field(
                        name=str(ucf_day_event.date[i]),
                        value="["
                        + str(ucf_day_event.name[i])
                        + "]"
                        + "("
                        + str(ucf_day_event.link[i])
                        + ")"
                        + " - "
                        + str(ucf_day_event.start_time[i]),
                        inline=True,
                    )
                await context.send(embed=event_message)
            except:
                await context.send(
                    "No events are currently this week, please refer to https://events.ucf.edu/event/ for the list"
                )


def setup(bot):
    bot.add_cog(UcfEvents(bot))
