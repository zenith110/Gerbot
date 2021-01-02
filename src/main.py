# imports what we need for the bot
# use pip install -r requirement.txt to install everything
from dotenv import load_dotenv
from os.path import join, dirname
import os
from discord import utils
import discord
from discord.ext import commands, tasks
from system_utils.command_builder import command_builder
from system_utils.debugger_switch import debugger_switch
from system_utils.debugger_option import debugger_option
from tasks.channel_purger import ChannelPurger

# import hidden variables
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Boolean that determines weather to use the console debugger or webhook similar to the container
prod_mode = True

# store values in global variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# creates bot instance as well as a command prefix
bot = commands.Bot("!")
bot.remove_command("help")
# terminal stuff
print("[!] Awakening Gerb's, standby...")
print("=" * 40)

# Switches all the prod_mode in all the cogs to the master prod_mode boolean here
debugger_switch(prod_mode)

try:
    command_builder(bot, prod_mode)
except:
    debugger_option(prod_mode)

# terminal functions
@bot.event
async def on_connect():
    print("[*] Client sucessfully connected to Discord")


"""
Task that purges channels that are inactive/no messages for longer than 30 days
Runs 24 hours and posts results to a channel
"""


@tasks.loop(hours=24)
async def channel_purger_run():
    channel_purge = await ChannelPurger(bot)


# upon successfully connecting to our server
@bot.event
async def on_ready():
    print("\n[*] Established bot onto server")
    print("-" * 40)
    channel_purger_run.start()
    # change the discord status because why not
    await bot.change_presence(activity=discord.Game(name="v1.0"))


# error handling whenever the command is not found
@bot.event
async def on_error(event, *args, **kwargs):
    container_logger()


bot.run(BOT_TOKEN)
