from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
from api_keys.discord_key import discord_key
app = Flask(__name__, static_url_path='/static')

@app.route("/update/", methods =["POST", "GET"])
def update_data():
    going_down = DiscordWebhook(url=discord_key, content='Gerbot going down for a bit')
    going_down_response = going_down.execute()

    print("Cleaning up old instances of gerbot")
    kill_process = subprocess.Popen(["sudo", "pkill", "-f", "main.py"], stdout=subprocess.PIPE)
    killoutput = kill_process.communicate()[0]

    print("Been pinged, let's update!")
    print("Beginning git pull")

    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    gitpull = process.communicate()[0]

    print("Git pull is done, now let's run the bot and the site!")
    up = DiscordWebhook(url=discord_key, content='Gerbot is up again!')
    up_response = up.execute()

    bot = subprocess.run(["sudo", "nohup", "python3", "main.py", "&", "sudo", "nohup", "python3", "app.py"], stdout=subprocess.PIPE)
    bot_info = bot.communicate()[0]
    return "Now running Gerbot!"	

@app.run("/run/", methods = ["POST", "GET"])    
def run():
    bot = subprocess.run(["sudo", "nohup", "python3", "main.py", "&", "sudo", "nohup", "python3", "app.py"], stdout=subprocess.PIPE)
    bot_info = bot.communicate()[0]
    return "Gerbot is running"
    
@app.route("/", methods =["POST", "GET"])
def index():
        return "Please use the routes to do commands"
        
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
