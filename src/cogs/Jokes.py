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
    async def GetJoke(self, context: discord.ext.commands.context.Context, *args: list):
        command_prefix = "!joke"
        command_name = "get joke"
        alias = "joke"
        example = "!joke (for a random joke), !joke <topic>"
        if not args:
            url = "https://icanhazdadjoke.com/"
            r = requests.get(url, headers={"Accept": "application/json"})
            data = r.json()
            joke_embed = discord.Embed(
                title=str(context.author) + "'s joke", description=data["joke"]
            )
            await context.send(embed=joke_embed)

        else:
            search_term = " ".join(args)
            url = "https://icanhazdadjoke.com/search"
            r = requests.get(
                url,
                headers={"Accept": "application/json"},
                params={"term": search_term},
            )
            data = r.json()
            total_jokes = data["total_jokes"]
            if total_jokes >= 1:
                rand_num = random.randint(0, total_jokes - 1)
                joke_embed = discord.Embed(
                    title=str(context.author) + "'s joke",
                    description=data["results"][rand_num]["joke"],
                )
                await context.send(embed=joke_embed)
            else:
                await context.send(f"Sorry, I couldn't find jokes on {search_term}.")


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Jokes(bot))
