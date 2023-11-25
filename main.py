#
#   AUTHOR:     BENJAMIN JOSEPH L. HERRERA
#

# Imports
import requests
from notion_client import Client

# Initialize Notion client
notion = Client(auth="YOUR_NOTION_INTEGRATION_TOKEN")

# Notion Kanban Database ID
database_id = "YOUR_DATABASE_ID"

# Discord Webhook URL
discord_webhook_url = "YOUR_DISCORD_WEBHOOK_URL"


# Get the response from Notion
def get_notion_updates():
    response = notion.databases.query(database_id)
    return response


# Post message information via the given Discord webhook
def post_to_discord(message):
    data = {"content": message}
    response = requests.post(discord_webhook_url, json=data)
    return response.status_code


# Main process
if __name__ == "__main__":
    # Get updates from Notion
    updates = get_notion_updates()

    # Create message
    message = "Latest Updates from Notion:\n" + str(updates)

    # Post the message
    post_to_discord(message)
