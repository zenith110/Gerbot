from os import name
from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord_key
import docker
import dockerhub_login
import datetime
import pytz  
app = Flask(__name__, static_url_path='/static')
@app.route("/update/", methods =["POST", "GET"])
def update_data():
    """
    Does some configuring for dockerhub
    """
    client = docker.from_env()
    client.login(username=dockerhub_login.username, password=dockerhub_login.password)

    going_down = DiscordWebhook(url=discord_key.api_key, content='Gerbot going down for a bit')
    going_down_response = going_down.execute()
    
    """
    If there's a docker instance, pull the latest image from the repo
    """
    try:
        client.images.pull(dockerhub_login.repo)
    # Removes the last instance and pulls the new one
    except:
        client.images.remove(dockerhub_login.repo + ":latest")
        client.images.pull(dockerhub_login.repo)

    # Attempts to deploys a docker container
    try:
        docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
    # If a docker container exist with the name, remove it and make a new instance
    except:
        ger = client.containers.get("ger")
        updating = DiscordWebhook(url=discord_key.api_key, content='Updating Gerbot container!')
        updating_response = updating.execute()
        ger.stop()
        client.containers.prune()
        subprocess.Popen("sudo", "killall", "./main.py")
        now = datetime.datetime.now(pytz.timezone('America/New_York'))
        if(now.hour > 12):
            hour = now.hour - 12
            up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again! Done at:\n' + str(hour) + ":" + str(now.minute) + "PM - " + str(now.day) + "/" + str(now.month) + "/" + str(now.year))
            docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
            up_response = up.execute()
        elif(now.hour < 12):
            up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again! Done at:\n' + str(now.hour) + ":" + str(now.minute) + " AM - " + str(now.day) + "/" + str(now.month) + "/" + str(now.year))
            up_response = up.execute()
            docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
     
    return "Now running Gerbot!"

def docker_stuff(client):
    try:
        docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
        return docker_container
    except:
        ger = client.containers.get("ger")
        ger.stop()
        ger.remove("ger")
@app.route("/run/", methods = ["POST", "GET"])    
def run():
    print("Showing instance of containers")
    return "Gerbot is running"
    
@app.route("/", methods =["POST", "GET"])
def index():
        return "Please use the routes to do commands"
        
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
