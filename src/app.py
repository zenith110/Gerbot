from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
from api_keys.discord_key import discord_key
app = Flask(__name__, static_url_path='/static')

@app.route("/update/", methods =["POST", "GET"])
def update_data():
    print("Cleaning up old instances of gerbot")
    kill_process = subprocess.Popen(["sudo", "pkill", "-f", "main.py"], stdout=subprocess.PIPE)
    killoutput = kill_process.communicate()[0]
    print("Been pinged, let's update!")
    print("Beginning git pull")
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    gitpull = process.communicate()[0]
    print("Git pull is done, now let's run the bot and the site!")
    bot = subprocess.run(["sudo", "nohup", "python3", "main.py", "&", "sudo", "nohup", "python3", "app.py"], stdout=subprocess.PIPE)
    bot_info = bot.communicate()[0]
    return "Now running Gerbot!"	
               
@app.route("/", methods =["POST", "GET"])
def index():
        return "Please use the routes to do commands"
        
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
