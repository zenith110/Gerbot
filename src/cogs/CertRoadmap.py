import certRoadmap
import discord
from discord.ext import commands

class CertRoadmap(commands.Cog):
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
    @name = specific roadmap
    return - nothing
    """
    @commands.command(aliases=['roadmap', 'map'])
    async def sendRoadmap(self, context, name):
        if name == "help":
            j = certRoadmap.getMapInfo("all")

            embed = discord.Embed(title="Roadmap Options", description="To see a map, use !map <name>")

            maps = ""

            for m in j:
                maps += f"{m['shortname']} - {m['name']}\n"
            
            await context.send(embed=embed)

        else:
            j = certRoadmap.getMapInfo(name)

            if j is False:
                # Add map names
                await context.send(f"{name} is not a valid map name!")
            else:
                embed = discord.Embed(title=f"Certification Roadmap for {j['name']}", description=f"Median annual salary: {j['annualSalary']}\nBuilt by {j['builtBy']}")
                
                certs = certRoadmap.getCerts(name)

                beginnerCerts = ""
                intermediateCerts = ""
                advancedCerts = ""
                expertCerts = ""

                # Loop through selected roadmap and sort by level
                for cert in certs:
                    if cert["level"] == "Beginner":
                        beginnerCerts += f"{cert['creator']} {cert['name']} - {cert['cost']}, Validity - {cert['validity']}\n"
                    if cert["level"] == "Intermediate":
                        intermediateCerts += f"{cert['creator']} {cert['name']} - {cert['cost']}, Validity - {cert['validity']}\n"
                    if cert["level"] == "Advanced":
                        advancedCerts += f"{cert['creator']} {cert['name']} - {cert['cost']}, Validity - {cert['validity']}\n"
                    if cert["level"] == "Expert":
                        expertCerts += f"{cert['creator']} {cert['name']} - {cert['cost']}, Validity - {cert['validity']}\n"

                embed.add_field(name="Beginner Certifications", value=("N/A" if beginnerCerts == "" else beginnerCerts), inline=False)
                embed.add_field(name="Intermediate Certifications", value=("N/A" if intermediateCerts == "" else intermediateCerts), inline=False)
                embed.add_field(name="Advanced Certifications", value=("N/A" if advancedCerts == "" else advancedCerts), inline=False)
                embed.add_field(name="Expert Certifications", value=("N/A" if expertCerts == "" else expertCerts), inline=False)

                await context.send(embed=embed)
                
                # for role in context.author.roles:
                #     print(role.name)

    # Prints information on cert <name>
    @commands.command(aliases=['cert'])
    async def sendCertInfo(self, context, name):
        cert = certRoadmap.getCertInfo(name)

        embed = discord.Embed(title=f"{cert['name']} Information")
        embed.add_field(name="Issuer", value=cert['creator'], inline=False)
        embed.add_field(name="Level", value=cert['level'], inline=False)
        embed.add_field(name="Cost", value=cert['cost'], inline=False)
        embed.add_field(name="Validity Period", value=cert['validity'], inline=False)
        embed.add_field(name="Website", value=cert['website'], inline=False)
        
        maps = ""

        for m in cert["plans"]:
            maps += f"{m}\n"

        embed.add_field(name="Included in", value=maps)

        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(CertRoadmap(bot))