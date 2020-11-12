# Gerbot

Gerbot is a python-based Discord bot written for the University of Central Florida's IT Discord. It's main functionality is to make our lives easier. It's private classroom functionality allows for the creation and management of private text channels modeled after technology classes that are accessible only by individuals with the corresponding class role. It has has some other quality of life features which are currently in development. The bot is primarily written in Python using discord.py


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
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Feel free to join the Discord at https://discord.gg/YM5QRzx <3

