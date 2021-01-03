import cyberstarter
import discord
from discord.ext import commands


class CyberStarter(commands.Cog):
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
    return - nothing
    """

    @commands.command(
        aliases=["cyber", "cyberstart", "cybersecstart", "cyberhelp", "cybersechelp"]
    )
    async def SendLinks(self, context: discord.ext.commands.context.Context):
        command_prefix = "!cyber"
        command_name = "Cyberstarter"
        alias = "cyber", "cyberstart", "cybersecstart", "cyberhelp", "cybersechelp"
        example = "!cyber"
        embeds = []
        j = cyberstarter.getFile()

        for s in j["sections"]:
            embed = discord.Embed(title=s["title"], description=s["description"])
            for f in s["fields"]:
                embed.add_field(name=f["name"], value=f["value"], inline=False)
                if not (f.get("image") is None):
                    embed.set_image(url=f["image"])

            embeds.append(embed)

        for embed in embeds:
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(CyberStarter(bot))
