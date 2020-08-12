import discord
import requests
from discord.ext import commands
import json
import dogs
class Dog(commands.Cog):
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
    @ctx - how we'll send messages
    @arg - arguments following the command
    return - nothing
    """
    @commands.command()
    async def getDog(self, context, arg):
        if(len(arg) > 0):
            try:
                dog = dogs.returnDog(arg)
                dog_name = dogs.getName(arg)
                dog_message = discord.Embed(title=dog_name + " image", description="Beep beep, I am a " + dog_name + " waiting to be booped!")
                dog_message.add_field(name="Image url", value=dog["message"])
                dog_message.set_image(url=dog["message"])
                await context.send(embed=dog_message)
            except:
                await context.send("The API we use doesn't have that breed, check out https://dog.ceo/dog-api/breeds-list for a full list")
        else:
            await context.send("Empty input provided, please pass in a breed!")
    

"""
setup for the command
"""
def setup(bot):
    bot.add_cog(Dog(bot))
    