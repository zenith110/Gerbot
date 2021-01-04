import discord
from discord.ext import commands
from discord.utils import get
import re
import cogs.Administration as admin
from disputils import BotEmbedPaginator


class Roles(commands.Cog):
    """
    Discord.py cog containing commands to faciliate the classroom role functionality.
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["r"])
    async def role(
        self,
        context: discord.ext.commands.context.Context,
        *,
        role: discord.Role = None,
    ):

        """
        Allows for Discord users to add, modify, remove, or inquire about roles on the server.
        """

        member = context.message.author
        command_prefix = "!role"
        command_name = "role"
        alias = "r"
        example = "!role <role-name>"
        # if the message author already has the role
        if role in member.roles:
            await member.remove_roles(role)
            await context.send(f"{member.mention}, took away that role.")

        # if !role returns no arguments
        elif role is None:
            await context.invoke(self.bot.get_command("PrintRoles"))

        else:
            await member.add_roles(role)
            await context.send(
                f"{member.mention}, you have been given the {role} role."
            )

    @role.error
    async def role_error(
        self, context: discord.ext.commands.context.Context, error: commands.BadArgument
    ):
        # if the !role argument wasn't valid
        if isinstance(error, commands.BadArgument):
            # strip the error for only the role name portion
            body = context.message.content.replace("!role ", "")
            member = context.message.author

            # valid classes must be detected in this format to be valid, and thus be created
            if re.search(r"\w+\d{4}c?-+\w", body):
                # create the class
                role = await admin.Administration.SpawnClass(self, context, body)
                await member.add_roles(role)
                await context.send(
                    f"{member.mention}, you're the first one in {body}. You have been given this role. Feel free to spread the word on your Webcourse's Discussions for this class."
                )

            else:
                await context.send(f"{member.mention} That role was not found.")

    @commands.command(aliases=["roles"])
    async def PrintRoles(self, context: discord.ext.commands.context.Context):
        """
        Command variant of the showRoles helper function; to diagnose showRoles bug on main server.
        """
        acl = [
            "Administrator",
            "Moderator",
            "@everyone",
            "Epic Counselor",
            "Sith-Gopher",
        ]

        # Creates a list of roles from the server that aren't in the acl.
        server_roles = [
            role.name for role in context.guild.roles if role.name not in acl
        ]

        # Uses regex and siphons out class roles from the server_roles list.
        class_roles = [o for o in server_roles if re.search("\d\d\d\d", o)]
        # Roles which are used for the server's squads.
        squad_roles = [o for o in server_roles if re.search("squad", o)]

        # Roles which are for certificaitons must have the checkmark to be able to be displayed correctly.
        cert_roles = [o for o in server_roles if re.search("🗸", o)]

        # Any roles not in the other lists will go here.
        misc_roles = [
            o
            for o in server_roles
            if o not in acl
            and o not in class_roles
            and o not in squad_roles
            and o not in cert_roles
        ]

        # splitting the class list into two separate lists for two embed entries
        list1 = class_roles[::2]
        list2 = class_roles[1::2]

        embeds = [
            discord.Embed(
                title="Squad Roles", description="\n".join(squad_roles), color=0x115599
            ),
            discord.Embed(
                title="Cert Roles", description="\n".join(cert_roles), color=0x5599FF
            ),
            discord.Embed(
                title="Class List 1", description="\n".join(list1), color=0x191638
            ),
            discord.Embed(
                title="Class List 2", description="\n".join(list2), color=0x191638
            ),
        ]

        # create the menu embed object
        paginator = BotEmbedPaginator(context, embeds)
        await paginator.run()


# Setup function
def setup(bot):
    bot.add_cog(Roles(bot))
