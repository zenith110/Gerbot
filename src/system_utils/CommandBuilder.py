import os
import json
import discord
from discord.ext import commands

"""
@word - Word use to search
@words - list of words that will be searched through
returns modified words list with the given words
"""


def CreateWordData(word: str, words: list):
    words = [match for match in words if word in match]
    words = [w.replace(word, "") for w in words]
    words = [w.replace('""', "") for w in words]
    words = [w.replace("\n", "") for w in words]
    words = [w.replace('"', "") for w in words]
    words = [w.strip() for w in words]
    return words


"""
Creates a command for the help command
"""


def LocalLoader(api_cogs: list, file_data: list, bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            file_directory = os.path.join("./cogs", filename)
            with open(file_directory, "r") as python_file:
                for lines in python_file:
                    file_data.append(lines)
            bot.load_extension(f"cogs.{filename[:-3]}")
            if filename in api_cogs:
                print(filename + " contains an api key, let's unload!")
                bot.unload_extension(f"cogs.{filename[:-3]}")
            print("[<3] Loaded ", filename)
    return file_data


def DefaultLoader(file_data: list, bot: discord.ext.commands.bot.Bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            file_directory = os.path.join("./cogs", filename)
            with open(file_directory, "r") as python_file:
                for lines in python_file:
                    file_data.append(lines)
            bot.load_extension(f"cogs.{filename[:-3]}")
            print("[<3] Loaded ", filename)
    return file_data


def CommandBuilder(bot: discord.ext.commands.bot.Bot, prod_mode: bool):
    file_data = []
    api_cogs = [""]
    if prod_mode == False:
        file_data = LocalLoader(api_cogs, file_data, bot)
    else:
        file_data = DefaultLoader(file_data, bot)

    name = CreateWordData("command_name = ", file_data)
    command_prefix = CreateWordData("command_prefix = ", file_data)
    data = {}
    data["commands"] = []
    for i in range(len(name)):
        data["commands"].append(
            {
                "command-prefix": command_prefix[i],
                "name": name[i],
            }
        )

    with open("commands.json", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=2)

