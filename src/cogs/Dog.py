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
    @context - how we'll send messages
    @arg - arguments following the command
    return - nothing
    """
    @commands.command()
    async def getDog(self, context, arg = None):
        """
        Fetches a dog breed using the provided input
        """
        if(arg is None):
            await context.send(f"{context.author.mention} seems you have provided no breed, try again!")
        else:
            try:

                dog = dogs.returnDog(arg.lower())
                dog_name = arg.lower()
                await context.send(f"{context.author.mention}, here is your {dog_name} that you asked for!")
                dog_message = discord.Embed(title=dog_name[0].upper() + dog_name[1:], description="Beep beep, I am a " + dog_name + " waiting to be booped!")
                dog_message.add_field(name="Image url", value=dog)
                dog_message.set_image(url=dog)
                await context.send(embed=dog_message)
            except:
                await context.send("The API we use doesn't have that breed, check out https://dog.ceo/dog-api/breeds-list for a full list")
    """
    returns all dogbreeds to a discord message
    @self - self obj
    @context - how we'll send messages
    returns - nothing
    """
    @commands.command()
    async def allDogs(self, context):
        """
        Gives a list of all the dog breeds available to be picked.
        """
        dog_obj = dogs.returnAll()
        dog_message = discord.Embed(title="Dog breeds", description="Beep beep, here's all the dog breeds that we have!")
        dog_message.add_field(name="All dog breeds", value=dog_obj, inline=True)
        await context.send(embed=dog_message)
        


"""
setup for the command
"""
def setup(bot):
    bot.add_cog(Dog(bot))
    