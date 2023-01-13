""" 
imports what we need for the bot
use pip install -r requirement.txt to install everything
"""
from dotenv import load_dotenv
from os.path import join, dirname
import os
import discord
from discord.ext import commands
from system_utils.CommandBuilder import CommandBuilder
from system_utils.DebuggerSwitch import DebuggerSwitch
from system_utils.DebuggerOption import DebuggerOption


"""
Loads the virtual enviroment
"""
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

"""
Boolean that determines weather to use the console debugger or webhook similar to the container
"""
prod_mode = True

"""
store values in global variables
"""
BOT_TOKEN = os.getenv("BOT_TOKEN")

"""
creates bot instance as well as a command prefix
"""
bot = commands.Bot("!")
bot.remove_command("help")

"""
terminal stuff
"""
print("[!] Awakening Gerb's, standby...")
print("=" * 40)
webhook_url = os.getenv("webhook_url")
"""
Switches all the prod_mode in all the cogs to the master prod_mode boolean here
"""
DebuggerSwitch(prod_mode)

try:
    CommandBuilder(bot, prod_mode)
except:
    DebuggerOption(prod_mode, webhook_url)


@bot.event
async def on_connect():
    print("[*] Client sucessfully connected to Discord")



"""
Upon successfully connecting to our server
"""


@bot.event
async def on_ready():
    print("\n[*] Established bot onto server")
    print("-" * 40)
    
    """
    Changes the discord status to the current release
    """
    await bot.change_presence(activity=discord.Game(name="Cleeping"))


"""
Error handling whenever the command is not found
"""


@bot.event
async def on_error(event, *args, **kwargs):
    DebuggerOption(prod_mode, webhook_url)


bot.run(BOT_TOKEN)
