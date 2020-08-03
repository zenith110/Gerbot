from dotenv import load_dotenv
from os.path import join, dirname
import os 
import discord
from discord.ext import commands
import parking

# import hidden variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# store values in global variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# creates bot instance as well as a command prefix
bot = commands.Bot("!")

# terminal stuff
print("[!] Awakening Gerb's, standby...")
print("="*40)

# import cogs 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("[<3] Loaded ", filename)

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

@bot.event
async def on_error(event, *args, **kwargs):
    print("[!] Error Caused by:  ", event)
    print(args, kwargs)


bot.run(BOT_TOKEN)