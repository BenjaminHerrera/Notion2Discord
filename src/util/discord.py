# Imports
from config.config import config, WEBHOOK_URL
from typing import List
import requests


def post_to_discord(
    title: str,
    message: str,
    image: str = None,
    fields: List[dict] = None,
) -> int:
    """Post Notion database item to a discord channel using channel webhooks.

    Args:
        title (str): Title of the database item
        message (str): Main content of the message
        image (str, optional): Cover of the item. Defaults to None.
        fields (List[dict], optional): Attributes to display. Defaults to None.

    Returns:
        int: Response code from Discord
    """

    # Prepare embed structure
    data = {
        "embeds": [
            {
                "title": title,
                "description": message,
                "color": config.color,
                "fields": fields,
                "image": {
                    "url": image,
                },
            }
        ],
        "username": config.name,
        "avatar_url": config.logo,
    }

    # Send and return response
    result = requests.post(WEBHOOK_URL, json=data)
    return result.status_code
