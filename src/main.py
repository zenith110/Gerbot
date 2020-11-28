# imports what we need for the bot
# use pip install -r requirement.txt to install everything
from dotenv import load_dotenv
from os.path import join, dirname
import os 
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord_key
import traceback
import datetime
import pytz 

# import hidden variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# store values in global variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# creates bot instance as well as a command prefix
bot = commands.Bot("!")
bot.remove_command('help')
# terminal stuff
print("[!] Awakening Gerb's, standby...")
print("="*40)
try:
    # import cogs 
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print("[<3] Loaded ", filename)
except:
    webhook = DiscordWebhook(url=discord_key.api_key)
    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    if(now.hour > 12):
        hour = now.hour - 12
        embed = DiscordEmbed(title='Error report on ' + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " - " + str(hour) + ":" + str(now.minute) + " PM", description = '```py\n%s\n```' % traceback.format_exc(), color=242424)
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        hour = now.hour - 12
        embed = DiscordEmbed(title='Error report on ' + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " - " + str(hour) + ":" + str(now.minute) + " AM", description = '```py\n%s\n```' % traceback.format_exc(), color=242424)
        webhook.add_embed(embed)
        response = webhook.execute()

# terminal functions
@bot.event
async def on_connect():
        print("[*] Client sucessfully connected to Discord")
# upon successfully connecting to our server
@bot.event
async def on_ready():
    print("\n[*] Established bot onto server")
    print("-"*40)

    # change the discord status because why not
    await bot.change_presence(activity=discord.Game(name="in development"))

# error handling whenever the command is not found
@bot.event
async def on_error(event, *args, **kwargs):
    print("hi")
    webhook = DiscordWebhook(url=discord_key.api_key)
    embed = DiscordEmbed(title='Error report', description = event, color=242424)
    webhook.add_embed(embed)
    response = webhook.execute()
    

bot.run(BOT_TOKEN)