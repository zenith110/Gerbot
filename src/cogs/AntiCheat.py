import discord
import re
from discord.ext import commands

class AntiCheat(commands.Cog):
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
    Scans every message for links to possible cheating websites if a user 
    is found cheating they are reported to the report channel      
    @self - self obj
    @message - the message being scanned by the function
    return - nothing
    """
    @commands.Cog.listener()
    async def on_message(self, message):
        """  
        Blacklist of known cheating websites
        """
        blacklist = ['chegg.com','coursehero.com']

        """  
        Setup the channel where the reports will be sent to
        """
        reportChannel = self.bot.get_channel(751495912299430020)
        cheating = 0

        """  
        Check if the message matches the items from the blacklist
        """
        for i in range(len(blacklist)):
            search = re.search(blacklist[i], message.content)
            if search != None:
                cheating = 1

        """  
        If the message is cheating a report will be sent to the report channel
        and the message will be deleted
        """
        if cheating == 1:
            print(message.content)
            embed = discord.Embed(title = 'User Report')
            embed.add_field(name = message.author, value = 'User has sent <' + message.content + '> in channel <' + str(message.channel) + '>', inline = True)
            await reportChannel.send(embed = embed)
            await self.bot.delete_message(message)
            

"""
setup for the command
"""
def setup(bot):
    bot.add_cog(AntiCheat(bot))