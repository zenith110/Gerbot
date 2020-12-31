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
    
    """
    Where the command is executed
    @self = self argument needed for the function
    @context = how we'll send messages
    @class_code = Class Code
    return - nothing
    """

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
                perm_settings = {
                    context.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    context.guild.me: discord.PermissionOverwrite(view_channel=True)
                }

                valid_roles = []
                valid = False
                class_role = None

                for role in context.guild.roles:
                    r = role.name.split("-")
                    x = re.match("([a-z][a-z][a-z]\d\d\d\d)", r[0])
                    if x != None:
                        valid_roles.append(role)

                for r in valid_roles:
                    name = r.name

                    if class_code == name:
                        valid = True
                        class_role = r
                        break

                if not valid:
                    await context.send(f"{class_code} is not a valid class")
                    return

                category = discord.utils.get(context.guild.categories, name="Study Rooms")

                channel = await context.guild.create_voice_channel(class_code, overwrites=perm_settings, category=category)
                await channel.set_permissions(class_role, view_channel=True)
                await context.send(f"Created study room for {class_code}")
            except:
                await context.send(f"Failed")
        
        return

def setup(bot):
    bot.add_cog(CustomStudyRoom(bot))