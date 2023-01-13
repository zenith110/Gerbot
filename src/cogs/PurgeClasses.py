import discord
from discord.ext import commands
import re


def return_position_server(server_list: list, server_name: str):
    index = 0
    for i in range(0, len(server_list)):
        if server_list[i].name == server_name:
            index = i
        else:
            continue
    return index


async def DeleteClasses(guild, name):
    categories = discord.utils.get(guild.categories, name=name)
    for channels in categories.channels:
        if re.search("([a-z][a-z][a-z]\d\d\d\d)", channels.name):
            role_object = discord.utils.get(guild.roles, name=channels.name)
            await role_object.delete()
            channel = discord.utils.get(guild.channels, name=channels.name)
            await channel.delete()


class PurgeClasses(commands.Cog):
    """
    Creates the instance of admin including its fields
    @bot - the bot itself
    @last_member - last member to use this
    return - nothing
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["purgeclasses", "pr"])
    @commands.has_role("Admin")
    async def PurgeClassChannels(self, ctx: discord.ext.commands.context.Context):
        server_index = return_position_server(self.bot.guilds, "UCF IT")
        guild = self.bot.guilds[server_index]
        await DeleteClasses(guild, "Classes 1")
        await DeleteClasses(guild, "Classes 2")

def setup(bot):
    bot.add_cog(PurgeClasses(bot))