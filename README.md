# Table of Contents
1. [Goal](#goal)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Creating a sample plugin](#creating-a-sample-plugin)
6. [Style guide](#style-guide)
    1. [Classes](#classes)
    2. [Functions](#functions)
    3. [Variables](#variables)
    4. [Commenting](#commenting)
7. [Gerbot tools](#tools)
    1. [Command Builder](#command-builder)
    2. [Production Mode](#production-mode)
## Goal
Gerbot is a python-based Discord bot written for the University of Central Florida's IT Discord. It's goal is to provide UCF IT majors with opportunities to socialize, study, and gain opportunities through various channels dedicated to organizations/interests.


## Installation

To install Gerbot on your machine, go ahead and clone the respository by doing:

```bash
git clone https://github.com/s1ag/Gerbot
```

Then go ahead and create a virtual environment with venv like so:

```bash
python3 -m venv env
```
Once the virtual environment has been created, activate it:

Linux:
```bash
source env/bin/activate
```
Window's 10:
```bash
.\env\Scripts\activate
```
Upon being activated you should see `(env)` besides your terminal. Now install the dependencies:

```bash
pip3 install -r requirements.txt 
```

## Usage
To use Gerbot, you must supply a valid bot token. First create a file in the `src directory` called `.env`. Inside this file populate it as follows: 

```bash
BOT_TOKEN=DISCORD_TOKEN_HERE
```
Finally, run main.py and you should see that your bot is now running :)

```bash
python3 main.py
```
While development should be done using the venv, persistent deployment can be accomplished by using the Dockerfile provided in the repo. 

## Contributing
You will need to first fork the repo, then submit a pull request that will be reviewed by the development team. 

For suggestions/concerns please submit an issues ticket. Feel free to join us and become part of the development community through here: https://discord.gg/YM5QRzx and post your inquiries/suggests in the #bot-chat channel. You may also request to join the team there as well.
 

## Creating a sample plugin

The plugins live within the cog directory, while the helper functions live outside the cog directory.

The code begins with imports 
```py
import discord 
from discord.ext import commands
```
Proceeded by a class based structure
```py
class Plugin(commands.Cog):
```

Create a init function within the class
```py
def __init__(self, bot):
  self.bot = bot
  self._last_member = None
 ```
 
 Use @commands.command to signify that it's a command, and assign it a list of aliases to use for others to reference upon:
 ```py
 @commands.command(aliases = ['example', 'test', 'sample'])
 ```
 Create a function, naming it anything. In this case, we'll call it first_plugin
 ```py
 async def simple_plugin(self, context, arg):
 ```
 Context is how we will send messages and access everything involving message data, async is referencing to async programming and is needed for discord.py to work. Arg is what will be passed in after our command. In this case it will be ping.
 
```py
if(arg == "ping"):
  await context.send("pong!")
```
We check to see if the argument passed is ping, and respond accordingly. 
To make sure that this plugin is loaded, we have to create a setup point like so:
```py 
def setup(bot):
    bot.add_cog(FirstPlugin(bot))
```
Full code:
```py
import discord
from discord.ext import commands
from system_utils.container_logger import container_logger
class FirstPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases = ['example', 'test', 'sample'])
    async def first_plugin(self, context):
        if(arg == "ping"):
            await context.send("pong")
        
def setup(bot):
    bot.add_cog(FirstPlugin(bot))
```

Congrulations! You've made your first plugin and dipped your toes into working with Gerbot.
## Style guide
Gerbot conforms to the PEP8 style, and enforces this using the black python plugin alongside with flake8. During contributing, follow these guidelines outline below as well. Black can be installed using:
```sh
pip install black
```
To format a file use:
```sh
black filename.py
```

To format an entire directory use:
```sh
black folder/
```

### Classes
All classes must follow a uppercase standard, this applies to cogs classes and the file names of these cogs as well. We do not follow snake case or camelcase for classes, and should refrain from doing so.
An example of this standard:
```sh
FileName.py
``` 
Opposed to:
```sh
fileName.py
```
Or:
```sh
file_name.py
```

### Functions
Functions will follow the same naming convention as classes, within the helper functions outside of cogs we will state the datatype explicilty. This is also true for helper functions as well.
An example:
```py
def function(string: str):
    print(string)
```

### Variables
Variables follow traditional snake case such as:
```py
test_string = str()
```
### Commenting
Gerbot style in regards to comment is following docstrings. 
Example:
```py
"""
This is a comment in the preferred way
"""
def comment(string: str):
    print(string)
```
### Tools
Gerbot has many some system utils that you may use to aid you in your development

#### Command Builder
This is an automated tool that will build commands.json for you, not requiring you to do so. To add your cog command data into the list, an example from the cog CustomStudyRoom.py is provided:
```py
@commands.has_permissions(manage_roles=True)
    async def CreateStudyRoom(self, context, class_code=None):
        command_prefix = "!sr"
        command_name = "Custom Study Room"
        alias = "createstudyroom, studyroom, sr"
        example = "!sr"
```
All that is necessary is to create variables for command_prefix, command_name, alias, and example and command builder will build your commands.json. 
Within command builder also lies the cog loader, which allows you to specify if you have any cogs that have apis to exclude, simply add it to the api_cogs list. The cat, and stock cogs are an example of cogs with apis.
Adding a cog to the list:
```py
"""
Before change
"""
api_cogs = ["Stocks.py", "Cat.py"]

"""
after change
"""
api_cogs = ["Stocks.py", "Cat.py", "Api.py"]
```

#### Production Mode
Within main.py lies a boolean, that will determine if it's in a deployed or development mode. If it's in development mode, certain features will be disabled for you, such as webhooks and will instead enable local debugging. It is preferable to disable when you are developing your features, and reenable when you have done a pull request. This variable is prod_mode, and can be toggled on or off.


