import discord
import requests
from discord.ext import commands
import weather


class Weather(commands.Cog):
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
    Fetches a city's weather forecast from the input      
    @self - self obj
    @context - how we'll send messages
    @*args - arguments following the command
    return - nothing
    """

    @commands.command(aliases=["weather"])
    async def GetWeather(
        self, context: discord.ext.commands.context.Context, *args: list
    ):
        command_prefix = "!weather"
        command_name = "weather"
        alias = "weather"
        example = "!weather <city-name>"
        """
        If no argument is given give the forecast for Orlando, Florida
        """
        if not args:
            ucf_forecast = weather.GetForecast("orlando")

            """
            Setup discord embed to send 
            """
            embed = discord.Embed(title="Weather Forecast")

            embed.add_field(
                name=ucf_forecast.name,
                value="Temperature: "
                + ucf_forecast.temperature
                + "\n"
                + "Description: "
                + ucf_forecast.description,
                inline=True,
            )

            await context.send(embed=embed)
        else:
            try:
                """
                From the arguments create a string that can be passed to the
                getForecast function
                """
                string = " ".join(args)

                ucf_forecast = weather.GetForecast(string)

                """
                Setup discord embed to send 
                """
                embed = discord.Embed(title="Weather Forecast")

                embed.add_field(
                    name=ucf_forecast.name,
                    value="Temperature: "
                    + ucf_forecast.temperature
                    + "\n"
                    + "Description: "
                    + ucf_forecast.description,
                    inline=True,
                )

                await context.send(embed=embed)
            except:
                """
                If the command is typed incorrectly display this message
                """
                await context.send(
                    'Forecast not found. Please try again using "!weather <cityname>"'
                )


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Weather(bot))
