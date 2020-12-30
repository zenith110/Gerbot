import discord
from discord.ext import commands

class CustomStudyRoom(commands.Cog):
    """
    sets up the basic components of the class
    @bot - the bot iself
    @last_member - the last member who used this command
    return - nothing
    """
    def __init__(self, bot):
        self.bot = bot 
        self._last_member = None

    """
    Where the command is executed
    @self = self argument needed for the function
    @context = how we'll send messages
    @class_code = Class Code
    return - nothing
    """

    @commands.command(aliases=['createstudyroom', 'studyroom'])
    async def createStudyRoom(self, context, class_code = None):
        # Create a new voice channel for class
        if discord.utils.get(context.guild.voice_channels, name=class_code):
            await context.send(f"Study room for {class_code} already exists")
            return
        
        try:
            category = discord.utils.get(context.guild.categories, name="Study Rooms")
            await context.guild.create_voice_channel(class_code, category=category)
            await context.send(f"Created study room for {class_code}")
        except:
            await context.send(f"Failed")
        
        return        

    # async def deleteChannel(self, context):
        # Delete the channel if everyone leaves

def setup(bot):
    bot.add_cog(CustomStudyRoom(bot))