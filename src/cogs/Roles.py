import discord
from discord.ext import commands
from discord.utils import get 
import re
import cogs.Administration as admin

class Roles(commands.Cog):
    """
    Discord.py cog containing commands to faciliate the classroom role functionality. 
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
 

    @commands.command()
    async def role(self, ctx, role: discord.Role = None):
        """
        Allows for Discord users to add, modify, remove, or inquire about roles on the server.
        """
    
        member = ctx.message.author
        
        # if the message author already has the role
        if role in member.roles:
            await  member.remove_roles(role)
            await ctx.send(f"{member.mention}, took away that role.")
        
        # if !role returns no arguments 
        elif role is None:
           embedded = showRoles(ctx)
           await ctx.send(embed=embedded)
        
        # gives user the valid, specified role
        else:
            await member.add_roles(role)
            await ctx.send(f"{member.mention}, you have been given the {role} role.")

    @role.error
    async def role_error(self, ctx, error):
        # if the !role argument wasn't valid
        if isinstance(error, commands.BadArgument):
            # strip the error for only the role name portion
            body = ctx.message.content.replace('!role ','')
            member = ctx.message.author
            
            # valid classes must be detected in this format to be valid, and thus be created
            if  re.search(r"[\w]+\d{4}[-]+\w", body):
                # create the class
                role = await admin.Administration.spawnClass(self, ctx, body)
                await member.add_roles(role)
                await ctx.send(f"{member.mention}, you're the first one in {body}. You have been given this role. Feel free to spread the word on your Webcourse's Discussions for this class.")

            else:
                await ctx.send(f"{member.mention} That role was not found.")


def showRoles(ctx):
    # Prohibited roles for regular users
    acl = ['Administrator', 'Moderator', '@everyone', 'Epic Counselor', 'Sith-Gopher']
    
    # Creates a list of roles from the server that aren't in the acl.
    server_roles = [role.name for role in ctx.guild.roles if role.name not in acl]
    
    # Uses regex and siphons out class roles from the server_roles list.
    class_roles=[o for o in server_roles if re.search('\d\d\d\d', o)]

    # Roles which are used for the server's squads.
    squad_roles=[o for o in server_roles if re.search("squad",o)]
    
    # Roles which are for certificaitons must have the checkmark to be able to be displayed correctly.
    cert_roles = [o for o in server_roles if re.search("🗸", o)]
    
    # Any roles not in the other lists will go here.
    misc_roles=[o for o in server_roles if o not in acl and o not in class_roles and o not in squad_roles and o not in cert_roles]        
    
    # Alphabetizes the list for clarity.
    class_roles.sort()
    squad_roles.sort()
    cert_roles.sort()
    misc_roles.sort()

    # Creates the embeded discord message. 
    embeded = discord.Embed(title="Roles")
    embeded.add_field(name="Classes", value = ("\n".join(class_roles)))
    embeded.add_field(name="Squad Roles", value = ("\n".join(squad_roles)))
    embeded.add_field(name="Certification Roles", value = ("\n".join(cert_roles)))
    embeded.add_field(name="Misc Roles", value = ("\n".join(misc_roles)))

# Pew pew, sends the embed to the chat
    return embeded

# Setup function
def setup(bot):
    bot.add_cog(Roles(bot))