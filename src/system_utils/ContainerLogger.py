import traceback
import datetime
import pytz
from discord_webhook import DiscordWebhook, DiscordEmbed

def ContainerLogger(webhook_url):
    webhook = DiscordWebhook(url=webhook_url)
    now = datetime.datetime.now(pytz.timezone("America/New_York"))
    if now.hour > 12:
        hour = now.hour - 12
        embed = DiscordEmbed(
            title="Error report on "
            + str(now.month)
            + "/"
            + str(now.day)
            + "/"
            + str(now.year)
            + " - "
            + str(hour)
            + ":"
            + str(now.minute)
            + " PM",
            description="```py\n%s\n```" % traceback.format_exc(),
            color=242424,
        )
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        hour = now.hour - 12
        embed = DiscordEmbed(
            title="@Bot-Dev Error report on "
            + str(now.month)
            + "/"
            + str(now.day)
            + "/"
            + str(now.year)
            + " - "
            + str(hour)
            + ":"
            + str(now.minute)
            + " AM",
            description="```py\n%s\n```" % traceback.format_exc(),
            color=242424,
        )
        webhook.add_embed(embed)
        response = webhook.execute()
