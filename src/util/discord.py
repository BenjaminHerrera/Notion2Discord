# Imports
from config.config import config, WEBHOOK_URL
import requests


# Post message information via the given Discord webhook
def post_to_discord(message, title=None, description=None, fields=None):
    # Prepare embed structure
    embed = {
        "title": title,
        "description": description,
        "color": 5097958,
        "fields": fields,
    }

    # Only include the embed if title or description is provided
    if title or description:
        data = {"embeds": [embed], "avatar_url": config.logo}
    else:
        data = {"content": message}

    # Send and return response
    return requests.post(WEBHOOK_URL, json=data).status_code
