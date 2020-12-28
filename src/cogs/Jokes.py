import discord
import random
import requests
from discord.ext import commands


class Jokes(commands.Cog):
    """
    Creates the instance of admin including its fields
    @bot - the bot itself
    @last_member - last member to use this
    return - nothing
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(pass_context=True, aliases=["joke", "dadJoke", "dadjoke"])
    async def getJoke(self, context, *args):
        if not args:
            url = "https://icanhazdadjoke.com/"
            r = requests.get(url, headers={"Accept": "application/json"})
            data = r.json()
            jokeEmbed = discord.Embed(
                title=str(context.author) + "'s joke", description=data["joke"]
            )
            await context.send(embed=jokeEmbed)

        else:
            searchTerm = " ".join(args)
            url = "https://icanhazdadjoke.com/search"
            r = requests.get(
                url, headers={"Accept": "application/json"}, params={"term": searchTerm}
            )
            data = r.json()
            totalJokes = data["total_jokes"]
            if totalJokes >= 1:
                randNum = random.randint(0, totalJokes - 1)
                jokeEmbed = discord.Embed(
                    title=str(context.author) + "'s joke",
                    description=data["results"][randNum]["joke"],
                )
                await context.send(embed=jokeEmbed)
            else:
                await context.send(f"Sorry, I couldn't find jokes on {searchTerm}.")


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Jokes(bot))
