from os import name
from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord_key
import docker
import dockerhub_login
from datetime import datetime
from pytz import timezone

app = Flask(__name__, static_url_path="/static")


@app.route("/gerbot/update/", methods=["POST", "GET"])
def update_data():
    """
    Does some configuring for dockerhub
    """
    client = docker.from_env()
    client.login(username=dockerhub_login.username, password=dockerhub_login.password)

    going_down = DiscordWebhook(
        url=discord_key.api_key, content="```Gerbot going down for a bit```"
    )
    going_down_response = going_down.execute()

    """
    If there's a docker instance, pull the latest image from the repo
    """
    try:
        pull = DiscordWebhook(
                url=discord_key.api_key,
                content="```Pulling a fresh image from dockerhub!```")
        pull_response = pull.execute()
        client.images.pull(dockerhub_login.repo)
    # Removes the last instance and pulls the new one
    except:
        delete_pull = DiscordWebhook(
                url=discord_key.api_key,
                content="```Now deleting and pulling the latest image!```")
        delete_pull_response = delete_pull_response.execute()        
        client.images.remove(dockerhub_login.repo + ":latest")
        client.images.pull(dockerhub_login.repo)

    docker_stuff(client)

    return "Now running Gerbot!"


def docker_stuff(client):
    try:
        docker_container = client.containers.run(
            dockerhub_login.repo + ":latest", name="ger"
        )
        return docker_container
    except:
        ger = client.containers.get("ger")
        stopping = DiscordWebhook(
                url=discord_key.api_key,
                content="```Now stopping gerbot and removing the current container!```")
        stopping_response = stopping.execute()         
        ger.stop()
        ger.remove()

        tz = timezone("EST")
        now = datetime.now(tz)

        up = DiscordWebhook(
                url=discord_key.api_key,
                content="```Gerbot is up again! Done at:\n"
                + str(now.month)
                + "/"
                + str(now.day)
                + "/"
                + str(now.year)
                + " - "
                + str(now.hour)
                + ":"
                + str(now.minute) + "```"
            )
        up_response = up.execute()
        docker_container = client.containers.run(
                dockerhub_login.repo + ":latest", name="ger"
            )
        


@app.route("/run/", methods=["POST", "GET"])
def run():
    print("Showing instance of containers")
    return "Gerbot is running"


@app.route("/", methods=["POST", "GET"])
def index():
    return "Please use the routes to do commands"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
