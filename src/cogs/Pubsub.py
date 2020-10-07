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
        if(sub_name != None):
            try:
                sub = pubsub.get_pub_sub(sub_name)
                original_sub_name = sub_name.replace("-", " ")
                sub_name_changed = sub_name.replace(" ", "-")
                if(sub.status == "True"):
                    await context.send(f"{context.author.mention}, here is your {original_sub_name}, it's on sale!")
                    pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
                    pubsub_message.add_field(name="Latest news on " + original_sub_name, value="Current sale last from " + last_sale + " with a price of " + price)
                    pubsub_message.set_image(url=sub.image)
                    await context.send(embed=pubsub_message)
                else:
                    await context.send("The sub you're looking for hasn't been on sale since " + sub.last_sale + "!")
            except:
                await context.send("Looks like " + sub_name + " isn't in the database yet, try again another time!")
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
                await context.send("The sub you're looking for hasn't been on sale since " + last_sale + "!")








def setup(bot):
    bot.add_cog(Pubsub(bot))