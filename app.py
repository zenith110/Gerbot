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
    print(client.images.list())
    if(docker.errors.ImageNotFound):
        print("Image not found!")
        print("Let's pull!")
        client.images.pull(dockerhub_login.repo)
    else:
         client.images.remove("zenith110/gerbot:latest")

    print(client.images.list())
    print("Making a new container based off this image...")
    if(not docker.errors.ImageNotFound):
        print("Container exist, let's remove it!")
        client.containers.remove(dockerhub_login.repo + ":latest")
    else:
        client.containers.create(dockerhub_login.repo + ":latest")
    
    
    

    print("Git pull is done, now let's run the bot and the site!")
    up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again!')
    up_response = up.execute()

    
    going_down = DiscordWebhook(url=discord_key.api_key, content='Gerbot is back')
    
    client.containers.run("zenith110/gerbot:latest")
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
