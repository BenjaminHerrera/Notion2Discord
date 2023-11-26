# Notion2Discord (N2D)
### Made with 💖 by Benjamin Herrera
N2D is a simple to use script that sends messages to a Discord channel for every
new update to the items in your Notion database!

## Dependencies
1. Any Linux Distribution
2. Docker (if not using in-house python packages)
3. Miniconda (if not using Docker)

## Setup Guide
This is going to be tedious, but bare with me! 😉👍
1. Git clone this repo
```bash
git clone https://github.com/BenjaminHerrera/Notion2Discord.git
```
2. Create a `.env` file in the `./` directory. It should have the following contents:
```bash
NOTION_INTEGRATION_TOKEN="..."
NOTION_DATABASE_ID="..."
DISCORD_WEBHOOK_URL="..."
```
3. Go to [your Notion integration page](https://www.notion.so/my-integrations) >>
`New Integration` >> Enter name for integration >> `Submit` >> Copy `Internal Integration Secret` >> Paste it as a value for the `NOTION_INTEGRATION_TOKEN` variable in
your `.env` file.
5. Go to your database on Notion >> Click on the three dots on the top right
of the page >> `Add connections` >> Select integration that you made.
7. Copy the database's link and extract the substring `<hash_1>` from this format:
```
https://www.notion.so/<hash_1>?v=<hash_2>
```
8. Place this substring as a value for the `NOTION_DATABASE_ID` variable in your
`.env` file.
9. Click on the gear icon next discord channel name >> `Integrations` >> `Webhooks` >> `New Webhook` >> Click on new webhook >> `Copy Webhook URL` >> Paste the URL into the value section of the `DISCORD_WEBHOOK_URL` variable in your `.env` file.
13. Now that you have your `.env` created, check the [Run Guide](https://github.com/BenjaminHerrera/Notion2Discord#run-guide) on how to
run the project.

## Run Guide

### If you want to use `DOCKER`

1. Run `docker compose up -d --build`

### If you want to use `PYTHON` with `CRONTAB` and `MINICONDA`

1. `cd notion2discord`
3. `./install.sh`

### If you want to use `PYTHON` with no repeat

1. `cd notion2discord`
2. `pip install -r requirements.txt`
3. `python main.py`