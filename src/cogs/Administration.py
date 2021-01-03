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
    @context - how we'll send the message
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def DeleteChan(self, context: discord.ext.commands.context.Context):
        try:
            await context.channel.delete()
        except:
            await context.channel.send("[!] Please check your syntax...")

    """
    deletes the role that is selected
    @self - self obj
    @context - how we'll send messages
    @arg - arguments following the command
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def DeleteRole(self, context: discord.ext.commands.context.Context, arg: str):
        # by default, delete the role with the same name as where the command is being ran (be careful)
        if arg is None:
            name = context.channel.name
            await context.invoke(self.bot.get_command("deleteRole"), arg=name.lower())

        # Deletes current channel
        else:
            try:
                role_name = arg.lower()
                role_object = discord.utils.get(context.message.guild.roles, name=role_name)
                await role_object.delete()
                await context.channel.send(f"[<3] Successfully deleted {role_name} role.")
            except:
                await context.channel.send("[!] Please check your role name")

    @commands.command()
    async def CreateRole(self, context: discord.ext.commands.context.Context, *args: list):
        for role in args:
            lower_name = role.lower()
            if discord.utils.get(context.guild.text_channels, name=lower_name):
                await context.channel.send(f"Channel {lower_name} already exists, aborting")
                return
            else:
                role = await context.guild.create_role(name=lower_name)
        await context.channel.send(f"Done creating the roles uwu.")

    """
    spawns a class
    @self - self obj
    @context - how we'll send messages
    @*arg - arguments following the command
    return - nothing
    """

    @commands.command(aliases=["sc", "spawn"])
    @commands.has_permissions(manage_roles=True)
    async def SpawnClass(self, context: discord.ext.commands.context.Context, *arg: str):
        command_prefix = "!spawn"
        command_name = "spawn class"
        alias = "spawn"
        example = "!spawn cop3502-gerber"
        # Make channel private
        custom_settings = {
            context.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            context.guild.me: discord.PermissionOverwrite(read_messages=True),
        }

        for name in arg:
            lower_name = name.lower()
            # Checks if class already exists
            if discord.utils.get(context.guild.text_channels, name=lower_name):
                await context.channel.send(f"Channel {lower_name} already exists, aborting")
                return
            try:

                # The category where the classes will go under
                category = discord.utils.get(context.guild.categories, name="Classes 1")

                channel = await context.guild.create_text_channel(
                    lower_name, overwrites=custom_settings, category=category
                )
                # Creates role with the same name as the channel
                role = await context.guild.create_role(name=lower_name)

                await channel.set_permissions(
                    role, send_messages=True, read_messages=True
                )
                await context.channel.send(
                    f"Created: {lower_name} channel and {lower_name} role"
                )
            except:
                await context.channel.send("[<3] Please check your syntax")
            return role

    """
    deletes channel and role
    @self - self object
    @context - how we'll send messages
    @name - name of role
    return - nothing
    """

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def DeleteAll(self, context: discord.ext.commands.context.Context, name: str = None):
        try:
            await context.invoke(self.bot.get_command("deleteRole"), arg=name)
            await context.invoke(self.bot.get_command("deleteChan"))
        except:
            await context.channel.send("[!] Check yo syntax")


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Administration(bot))
