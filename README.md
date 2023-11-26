# Notion2Discord (N2D)
N2D is a simple to use script that sends messages to a Discord channel for every
new update to the items in your Notion database!

## Setup Guide
This is going to be tedious, but bare with me! 😉👍
1. Create a `.env` file in the root directory. It should have the following contents:
```bash
NOTION_INTEGRATION_TOKEN="..."
NOTION_DATABASE_ID="..."
DISCORD_WEBHOOK_URL="..."
```
2. Go to [your Notion integration page](https://www.notion.so/my-integrations)
3. Click on `New Integration`, Create a name for this integration, and
then press `submit`.
4. Copy the `Internal Integration Secret` key and paste it as a value for the
`NOTION_INTEGRATION_TOKEN` variable in your `.env` file.
5. Go to your database on Notion and click on the three dots on the top right
of the page.
6. Look for `Add connections`, click it, search for the integration that you made,
and select it.
7. Copy the database's link and extract the substring `<hash_1>` from this format:
```
https://www.notion.so/<hash_1>?v=<hash_2>
```
8. Place this substring as a value for the `NOTION_DATABASE_ID` variable in your
`.env` file.
9. Go to the Discord Channel that you want to send updates to and click on the
gear icon next to its name when you hover over it.
10. Go to `Integrations`, click on `Webhooks`, then `New Webhook`.
11. Click on the new webhook that was created for you and click `Copy Webhook URL`.
12. Paste the URL you copied into the value section of the `DISCORD_WEBHOOK_URL`
variable in your `.env` file.