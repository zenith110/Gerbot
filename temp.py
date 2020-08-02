from dotenv import load_dotenv
from os.path import join, dirname
import os 
import discord
from discord.ext import commands
from discord.utils import find

import parking
import asyncio

# import hidden variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Gerbot(discord.Client):
    
    def __init__(self):
        bot = commands.Bot
        self.load_shit()



    print("[!] Awakening Gerb's, standby...")
    print("="*40)

    # def load_cogs(self, ctx):
    #     self.load_extensions(f'cogs.{ctx}')

    # def unload_cogs(self, ctx):
    #     self.unload_extensions(f'cogs.{ctx}')
        

    def load_shit(self):    
        for filename in os.listdir('./cogs'):
            print(filename)
            if filename.endswith('.py'):
                self.load_extension(f'cogs.{filename[:-3]}')
                print(f"Sucessfully imported cog.{filename}")
            else:
                print("no dice")



if __name__ == '__main__':
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    bot = Gerbot()
    
    bot.run(BOT_TOKEN)