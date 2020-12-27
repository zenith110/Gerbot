import discord

# import parking
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

"""
creates the class for admin commands
"""


class Administration(commands.Cog):
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
    command that deletes the channel
    checks the permission of the user before deleting it
    @self - self obj
    @ctx - how we'll send the message
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deleteChan(self, ctx):
        try:
            await ctx.channel.delete()
        except:
            await ctx.channel.send("[!] Please check your syntax...")

    """
    deletes the role that is selected
    @self - self obj
    @ctx - how we'll send messages
    @arg - arguments following the command
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deleteRole(self, ctx, arg):
        # by default, delete the role with the same name as where the command is being ran (be careful)
        if arg is None:
            name = ctx.channel.name
            await ctx.invoke(self.bot.get_command("deleteRole"), arg=name.lower())

        # Deletes current channel
        else:
            try:
                role_name = arg.lower()
                role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
                await role_object.delete()
                await ctx.channel.send(f"[<3] Successfully deleted {role_name} role.")
            except:
                await ctx.channel.send("[!] Please check your role name")

    @commands.command()
    async def createRole(self, ctx, *args):
        for role in args:
            lowername = role.lower()
            if discord.utils.get(ctx.guild.text_channels, name=lowername):
                await ctx.channel.send(f"Channel {lowername} already exists, aborting")
                return
            else:
                role = await ctx.guild.create_role(name=lowername)
        await ctx.channel.send(f"Done creating the roles uwu.")

    """
    spawns a class
    @self - self obj
    @ctx - how we'll send messages
    @*arg - arguments following the command
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def spawnClass(self, ctx, *arg):
        # Make channel private
        custom_settings = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        }

        for name in arg:
            lowername = name.lower()
            # Checks if class already exists
            if discord.utils.get(ctx.guild.text_channels, name=lowername):
                await ctx.channel.send(f"Channel {lowername} already exists, aborting")
                return
            try:

                # The category where the classes will go under
                category = discord.utils.get(ctx.guild.categories, name="Classes 1")

                channel = await ctx.guild.create_text_channel(
                    lowername, overwrites=custom_settings, category=category
                )
                # Creates role with the same name as the channel
                role = await ctx.guild.create_role(name=lowername)

                await channel.set_permissions(
                    role, send_messages=True, read_messages=True
                )
                await ctx.channel.send(
                    f"Created: {lowername} channel and {lowername} role"
                )
            except:
                await ctx.channel.send("[<3] Please check your syntax")
            return role

    """
    deletes channel and role
    @self - self object
    @ctx - how we'll send messages
    @name - name of role
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deleteAll(self, ctx, name=None):
        try:
            await ctx.invoke(self.bot.get_command("deleteRole"), arg=name)
            await ctx.invoke(self.bot.get_command("deleteChan"))
        except:
            await ctx.channel.send("[!] Check yo syntax")


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Administration(bot))
