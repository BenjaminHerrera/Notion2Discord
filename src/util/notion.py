# Imports
from config.config import NOTION, DATABASE_ID


# Get the response from Notion
def get_notion_updates():
    response = NOTION.databases.query(DATABASE_ID)
    return response
