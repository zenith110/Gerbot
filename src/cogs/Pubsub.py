import discord
from discord.ext import commands
import pubsub
import json
import re
class Pubsub(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def getPubsub(self, context, *, sub_name = None):
        """
        Fetches a delicious pubsub
        """
        if(sub_name != None):
            sub = pubsub.get_pub_sub(sub_name)
            if(sub.status_code == "OK"):
                original_sub_name = sub_name.replace("-", " ")
                sub_name_changed = sub_name.replace(" ", "-")
                if(sub.status == "True"):
                    await context.send(f"{context.author.mention}, here is your {original_sub_name}, it's on sale!")
                    pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                    pubsub_message.add_field(name="Latest news on " + original_sub_name, value="Current sale last from " + sub.last_sale + " with a price of " + sub.price)
                    pubsub_message.set_image(url=sub.image)
                    await context.send(embed=pubsub_message)
                else:
                    pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                    pubsub_message.add_field(name="Last time " + original_sub_name + " was on sale", value="Last sale was from " + sub.last_sale)
                    pubsub_message.set_image(url=sub.image)
                    await context.send(embed=pubsub_message)
            elif(sub.status_code == "404"):
                await context.send("The pubsub api does not contain that sub, please try another sub!")
        else:
            sub = pubsub.empty_sub_input()
            sub_name = sub.sub_name
            last_sale = sub.last_sale
            status = sub.status
            price = sub.price
            image = sub.image
            sub_name = sub_name.replace("-", " ")
            if(status == "True"):
                await context.send(f"{context.author.mention}, here is your {sub_name}, it's on sale!")
                pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                pubsub_message.add_field(name="Latest news on " + sub_name, value="Current sale last from " + last_sale + " with a price of " + price)
                pubsub_message.set_image(url=image)
                await context.send(embed=pubsub_message)
            else:
                pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                pubsub_message.add_field(name="Last time " + sub_name + " was on sale", value="Last sale was from " + sub.last_sale)
                pubsub_message.set_image(url=sub.image)
                await context.send(embed=pubsub_message)

    
    @commands.command()
    async def subs(self, context):
        """
        Gets the names of all the pubsubs
        """
        subs = pubsub.get_all_subs()
        await context.send(f"{context.author.mention}, here is our list of subs! \n" + subs)









def setup(bot):
    bot.add_cog(Pubsub(bot))