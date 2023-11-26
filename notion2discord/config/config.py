# Import(s)
from util.dict_obj import DictObj
from notion_client import Client
from dotenv import load_dotenv
import json
import os

# Load environment variables from .env file
load_dotenv()

# Export CONSTANTS
NOTION = Client(auth=os.getenv("NOTION_INTEGRATION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Export configs
config = DictObj(json.load(open("./config/config.json")))
