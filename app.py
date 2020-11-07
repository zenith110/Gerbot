from os import name
from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord_key
import docker
import dockerhub_login
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
    
    if(docker.errors.ImageNotFound):
        client.images.pull(dockerhub_login.repo)
    else:
         client.images.remove("zenith110/gerbot:latest")


    try:
       print("Container doesn't exist, let's make it!")
       up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again!')
       up_response = up.execute()
       client.containers.run(dockerhub_login.repo + ":latest", name="ger") 
    except:
       print("Container exist, let's remove it!")
       updating = DiscordWebhook(url=discord_key.api_key, content='Updating Gerbot container!')
       updating_response = updating.execute()
       client.containers.stop("ger")
       client.containers.remove("ger")
       up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again!')
       up_response = up.execute()
       client.containers.run(dockerhub_login.repo + ":latest", name= "ger")

        
    subprocess.Popen("sudo", "nohup", "python3", "app.py", stdout=subprocess.PIPE)
    return "Now running Gerbot!"	

@app.route("/run/", methods = ["POST", "GET"])    
def run():
    print("Showing instance of containers")
   
    
    return "Gerbot is running"
    
@app.route("/", methods =["POST", "GET"])
def index():
        return "Please use the routes to do commands"
        
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
