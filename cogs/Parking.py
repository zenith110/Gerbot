import discord
from discord.ext import commands
import parking

class Parking(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def parkingInfo(self, context):
        
        soup = parking.getGarageSite()
        maxSpots = parking.getMaxSpots(soup)
        spotsLeft = parking.getSpotsLeft(soup)
        names = parking.getGarageNames(soup)

        await context.author.create_dm()
    
        for i in range(len(names)):
            await context.author.dm_channel.send(f"""```{names[i]}    : {spotsLeft[i]} / {maxSpots[i]} | {abs(maxSpots[i] - spotsLeft[i])} Spots Taken ~ {abs(100 - (spotsLeft[i]/maxSpots[i] * 100)): .0f}% Full```""")



def setup(bot):
    bot.add_cog(Parking(bot))
    