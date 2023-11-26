# Imports
from config.config import NOTION, DATABASE_ID
from typing import List


def get_notion_updates() -> List[dict]:
    """Retrieve database contents based on the given database ID

    Returns:
        List[dict]: List of items on the database
    """

    # Return the contents of the database
    return NOTION.databases.query(DATABASE_ID)["results"]
