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
        print("Pulling the latest image")
        client.images.pull(dockerhub_login.repo)
    else:
        client.images.remove("zenith110/gerbot:latest")

    print("Let's make the container")
    try:
        docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
        return docker_container
    except:
        ger = client.containers.get("ger")
        updating = DiscordWebhook(url=discord_key.api_key, content='Updating Gerbot container!')
        updating_response = updating.execute()
        ger.stop()
        ger.remove()
        up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again!')
        up_response = up.execute()
        docker_container = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
   
    # print(" hi" + str(ger))
    # if(ger == docker.errors.ImageNotFound):
    #     print("Let's let the containers be shown!")
    #     ger.stop()
    #     ger.remove("ger")
        # ger = client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
        # print("Let's let the containers be shown!")
        # ger.stop()
        # ger.remove("ger")
    
    
    # if(docker.errors.ImageNotFound):
    #     print("If this exist already, return error and let's get going!")
    #     print("Container exist, let's remove it!")
    #     updating = DiscordWebhook(url=discord_key.api_key, content='Updating Gerbot container!')
    #     updating_response = updating.execute()
    #     for container in client.containers.list():
    #             container.stop()
    #     print(ger)
    #     ger.remove("ger")
    #     print("Stopped the container, let's remove it now!")
        up = DiscordWebhook(url=discord_key.api_key, content='Gerbot is up again!')
        up_response = up.execute()
    #     client.containers.run(dockerhub_login.repo + ":latest", name= "ger")
   
     
    # subprocess.Popen("sudo", "nohup", "python3", "app.py", stdout=subprocess.PIPE)
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
