# Imports
from util.discord import post_to_discord
from util.notion import get_notion_updates
import pprint

# Main process
if __name__ == "__main__":
    # Get updates from Notion
    updates = get_notion_updates()

    # Iterate through the cards in your database
    for i in updates["results"]:
        if i["cover"] is not None:
            pprint.pprint(i)

    # Create message
    message = "Latest Updates from Notion:\n" + str(1)

    # Post the message
    post_to_discord("Test", message)
