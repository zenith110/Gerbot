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
    async def getPubSub(self, context, *, sub_name):
        sub = pubsub.get_pub_sub(sub_name)
        original_sub_name = sub_name.replace("-", " ")
        sub_name_changed = sub_name.replace(" ", "-")
        within = sub[sub_name_changed][0]
        sub_name = within["sub_name"]
        last_sale = within["last_sale"]
        status = within["status"]
        price = within["price"]
        image = within["image"]
        if(status == "True"):
            pubsub_message = discord.Embed(title="Latest deal for pubsubs" , description="Beep beep, I bring you the most current pubsub deals!")
            pubsub_message.add_field(name="Latest news on " + original_sub_name, value="Current sale last from " + last_sale + " with a price of " + price)
            pubsub_message.set_image(url=image)
            await context.send(embed=pubsub_message)
        else:
            await context.send("The sub you're looking for hasn't been on sale since " + last_sale + "!")








def setup(bot):
    bot.add_cog(Pubsub(bot))