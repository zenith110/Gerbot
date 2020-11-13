from os import error
import discord
import requests
from discord.ext import commands
import weather
import json
import os
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
    @commands.command(aliases = ['help', 'commands'])
    async def helpSystem(self, context, *args):
        """
        Open the commands json file that has all of our commands
        """
        with open("commands.json") as json_file:
            commands = json.load(json_file)
        """
        Assign the json instance to a variable
        """
        commands_link = commands["commands"]

        help_message = discord.Embed(title="Gerbot Commands", description="Commands available to Gerbot!")
        data = []
        
        for i in range(len(commands_link)):
            names = ", ".join(commands_link[i]["names"])
            sub_arguments = ", ".join(commands_link[i]["sub-commands"])
            
            data.append("**" + commands_link[i]["name"] + "** - " + commands_link[i]["example"] + "\n" + commands_link[i]["description"] + "\n" + "Aliases: [" + names + "]" + "\nSub Arguments: [" + sub_arguments + "]\n")

        value_string = "\n".join(data)

        help_message.add_field(name="Commands", value=value_string, inline=True)

        help_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif")
        
        await context.send(embed=help_message)
"""
setup for the command
"""
def setup(bot):
    bot.add_cog(Weather(bot))