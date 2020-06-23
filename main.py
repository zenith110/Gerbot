from dotenv import load_dotenv
from os.path import join, dirname
import os 
import discord
from discord.ext import commands
import parking

# import hidden variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# store values in global variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
SERVER= os.getenv('DISCORD_SERVER')

# creates bot instance as well as a command prefix
bot = commands.Bot("!")

# terminal stuff
print("[!] Awakening Gerb's, standby...")
print("="*40)


@bot.event
async def on_connect():
        print("[*] Client sucessfully connected to Discord")
# upon successfully connecting to our server
@bot.event
async def on_ready():
    print("\n[*] Established bot onto server")
    print("-"*40)

    # change the discord status because why not
    await bot.change_presence(activity=discord.Game(name="in development"))

@bot.event
async def on_error(event, *args, **kwargs):
    print("[!] Error Caused by:  ", event)
    print(args, kwargs)


@bot.command()
async def hello(ctx):
    print(ctx.author)
    await ctx.channel.send("Hello")

# create class channel
#     channel = await name.guild.create_text_channel(name.message.content)


#create new channel
@bot.command()
async def spawn(ctx, arg):
    overwrites = {
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    channel = await ctx.guild.create_text_channel(arg, overwrites=overwrites)
    print("Spawned: ", arg)

# @bot.command()
# async def whoami(ctx):
    
@bot.command(pass_context=True)
async def move(ctx):
    # channel = bot.get_channel(arg, )
    await bot.move_member(ctx.message.author, 723942191835250748)

@bot.command() 
async def clone(ctx):
    print(ctx.channel)
    await ctx.channel.clone()

@bot.command()
async def delete(ctx):
    print("Deleted: ", ctx.channel)
    await ctx.channel.delete()

@bot.command()
async def parkingInfo(context):
    if context.author == bot.user:
        return
    
    soup = parking.getGarageSite()
    maxSpots = parking.getMaxSpots(soup)
    spotsLeft = parking.getSpotsLeft(soup)
    names = parking.getGarageNames(soup)

    # user = bot.get_user(context.author.id)
    # await user.crea te_dm()
    await context.author.create_dm()
 
    for i in range(len(names)):
        await context.author.dm_channel.send(f"""```{names[i]}    : {spotsLeft[i]} / {maxSpots[i]} | {abs(maxSpots[i] - spotsLeft[i])} Spots Taken ~ {abs(100 - (spotsLeft[i]/maxSpots[i] * 100)): .0f}% Full```""")



bot.run(BOT_TOKEN)