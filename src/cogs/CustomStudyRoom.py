import discord
from discord.ext import commands, tasks
from datetime import datetime
import re

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
        # self.deleteUnusedChannels.start()

    # def cog_unload(self):
        # self.deleteUnusedChannels.cancel()

    
    """
    Where the command is executed
    @self = self argument needed for the function
    @context = how we'll send messages
    @class_code = Class Code
    return - nothing
    """


    # @tasks.loop(seconds=15.0)
    # async def deleteUnusedChannels(self, context):
    #     print("deleting unused channes")
    #     category = discord.utils.get(context.guild.categories, name="Study Rooms")

    #     for c in category.channels:
    #         elapsed = c.created_at - datetime.now()

    #         if len(c.members) < 1 and elapsed / 60 > 15:
    #             await c.delete()

    @commands.command(aliases=['createstudyroom', 'studyroom', 'sr'])
    @commands.has_permissions(manage_roles=True)
    async def createStudyRoom(self, context, class_code = None):
        # Create a new voice channel for class
        if discord.utils.get(context.guild.voice_channels, name=class_code):
            await context.send(f"Study room for {class_code} already exists")
            return
        
        if class_code is None:
            roles = context.author.roles
            classes = []

            for role in roles:
                r = role.name.split("-")
                x = re.match("([a-z][a-z][a-z]\d\d\d\d)", r[0])
                if x != None:
                    classes.append(role.name)

            class_string = ""

            for c in classes:
                class_string = class_string + f"{c}\n"
            
            embed = discord.Embed(title="Classes", description="To create a study room, use !studyroom <role>")
            embed.add_field(name="You have the following classes:", value=class_string)

            await context.send(embed=embed)
        else:
            try:
                valid_roles = []

                for role in context.guild.roles:
                    r = role.name.split("-")
                    x = re.match("([a-z][a-z][a-z]\d\d\d\d)", r[0])
                    if x != None:
                        valid_roles.append(role.name)

                if not class_code in valid_roles:
                    await context.send(f"{class_code} is not a valid class")
                    return

                category = discord.utils.get(context.guild.categories, name="Study Rooms")

                await context.guild.create_voice_channel(class_code, category=category)
                await context.send(f"Created study room for {class_code}")
            except:
                await context.send(f"Failed")
        
        return

    # @commands.command(aliases=["test"])
    # async def detail(self, context):
    #     category = discord.utils.get(context.guild.categories, name="Study Rooms")

    #     for c in category.channels:
    #         print(f"{c.name} created at {c.created_at} has {len(c.members)} users connected")
            
    #         elapsed = c.created_at - datetime.now()
    #         elapsed_min = elapsed.total_seconds() / 60
    #         print(elapsed_min)

def setup(bot):
    bot.add_cog(CustomStudyRoom(bot))