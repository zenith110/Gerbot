import discord
from discord.ext import commands
import pubsub
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
    async def getPubSub(self, context):
        sub = pubsub.get_pub_sub()
        pubsub_message = discord.Embed(title="Latest pubsub deal", description="Beep beep, I bring you the most current pubsub deals! \nFollow @PubSubs_on_sale")
        pubsub_message.add_field(name="Latest pubsub deal offering", value=sub)
        await context.send(embed=pubsub_message)







def setup(bot):
    bot.add_cog(Pubsub(bot))