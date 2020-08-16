import discord
from discord.ext import commands
import stocks
class Stocks(commands.Cog):
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
    async def getStock(self, context, argument = None):
        """
        Returns the name of the stock, and some information about it
        """
        if(argument is None):
            await context.send("It seems you have not provided a stock, try again")
        else:
            argument = argument.upper()
            stonk = stocks.basic_stock_return(argument)
            try:
                stonk_message = discord.Embed(title=stonk.name + " stonk report", description="Data information about " + stonk.name + " stock")
                stonk_message.add_field(name="Stock data", value="**Current price**: $" + str(stonk.current_price) + "\n**Open price of the day**: $" + str(stonk.open_price) + "\n**Low price of the day**: $" + str(stonk.low_price), inline=True)       
                await context.send(embed=stonk_message)
            except:
                await context.send("It seems the stock you have tried to use is not a proper stock, please try again")

def setup(bot):
    bot.add_cog(Stocks(bot))