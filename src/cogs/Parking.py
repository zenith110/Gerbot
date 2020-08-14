import discord
from discord.ext import commands
import parking
import math
"""
Allows us to spit out the data for parking data
"""
class Parking(commands.Cog):
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
    @commands.command()
    
    async def parkingInfo(self, context):
        """
        Used to return UCF parking garage data
        """
        soup = parking.getGarageSite()
        maxSpots = parking.getMaxSpots(soup)
        spotsLeft = parking.getSpotsLeft(soup)
        names = parking.getGarageNames(soup)

        """
        Creates the DM for the user who invoked the command
        """
        await context.author.create_dm()

        """
        Enables a discord embed so we can send the data nicely
        """
        garage = discord.Embed(title="Parking Statistics", description="Beep beep, I bring you the latest in UCF parking data.")

        """
        Loops through the name data so we can assign the data to each garage
        """
        for i in range(len(names)):
            """
            Adds the data to a discord rich embed message
            """
            garage.add_field(name=names[i], value=(str(spotsLeft[i]) + "/" +  str(maxSpots[i]) + " | " +  str(abs(maxSpots[i] - spotsLeft[i])) + " Spots available ~ " + str(math.floor(abs(100 - (spotsLeft[i]/maxSpots[i] * 100)))) + "%" +  " Empty"))

        """
        Sends out the message to the user who pinged the command
        """
        await context.author.dm_channel.send(embed=garage)

"""
Calls the parking command
"""
def setup(bot):
    bot.add_cog(Parking(bot))
    