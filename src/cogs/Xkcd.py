import discord
import requests
from discord.ext import commands
import json
import xkcd


class Xkcd(commands.Cog):
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
    deletes the role that is selected
    @self - self obj
    @context - how we'll send messages
    @comic_num - arguments following the command
    return - nothing
    """

    @commands.command(pass_context=True, aliases=["xkcd"])
    async def GetComic(self, context, comic_num=None):
        command_prefix = "!xkcd"
        command_name = "get comic"
        alias = "xkcd"
        example = "!xkcd (for today's comic), !xkcd <comic-number>"
        """
        If argument is empty, get today's comic
        """
        if comic_num is None:
            comic = xkcd.GetTodayComic()
            comic_title = comic["title"]
            comic_text = comic["alt"]
            comic_picture = comic["img"]
            await context.send(f"{context.author.mention}, here is today's xkcd comic!")
            comic_message = discord.Embed(title=comic_title, description=comic_text)
            comic_message.add_field(name="Image url", value=comic_picture)
            comic_message.set_image(url=comic_picture)
            await context.send(embed=comic_message)
        else:
            comic = xkcd.GetComic(comic_num)
            comic_title = comic["title"]
            comic_text = comic["alt"]
            comic_picture = comic["img"]
            await context.send(
                f"{context.author.mention}, here is a xkcd comic {comic_num}!"
            )
            comic_message = discord.Embed(title=comic_title, description=comic_text)
            comic_message.add_field(name="Image url", value=comic_picture)
            comic_message.set_image(url=comic_picture)
            await context.send(embed=comic_message)

    @commands.command(pass_context=True, aliases=["randxkcd"])
    async def getRandomComic(self, context):
        command_prefix = "!randxkcd"
        command_name = "get random comic"
        alias = "randxkcd"
        example = "!randxkcd"
        """
        Gets a random xkcd comic
        """
        comic = xkcd.GetRandomComic()
        comic_title = comic["title"]
        comic_text = comic["alt"]
        comic_picture = comic["img"]
        await context.send(
            f"{context.author.mention}, here is a random xkcd comic! (#{comic['num']})"
        )
        comic_message = discord.Embed(title=comic_title, description=comic_text)
        comic_message.add_field(name="Image url", value=comic_picture)
        comic_message.set_image(url=comic_picture)
        await context.send(embed=comic_message)


def setup(bot):
    bot.add_cog(Xkcd(bot))
