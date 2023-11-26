# Imports
from util.notion import get_notion_updates
from util.discord import post_to_discord
from util.dict_obj import DictObj
from util.time import transform_datetime
from config.config import config
from pprint import pprint  # noqa

# Main process
if __name__ == "__main__":
    # Iterate through the cards in your database
    for item in get_notion_updates()[: config.dispatch_limit]:
        # Reset tracking variables
        item_name = ""
        image = None
        fields = []

        # Wrap dict in DictObj
        item = DictObj(item)

        # ! DEBUG
        # pprint(item)

        # Place image if it exists
        if item.cover is not None:
            image = item.cover.file.url

        # Iterate through the item's properties
        for key in item.properties:
            # If the iterated key is the title, save the title name
            if "title" in item.properties[key]:
                item_name = item.properties[key].title[0]["plain_text"]

            # If the iterated key is of type PEOPLE
            if "people" in item.properties[key]:
                # Format the value
                value = ", ".join(
                    [i["name"] for i in item.properties[key].people]
                )
                if not value:
                    value = config.empty_value

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type CHECKBOX
            if "checkbox" in item.properties[key]:
                # Format the value
                value = (
                    config.checkbox_true
                    if item.properties[key].checkbox
                    else config.checkbox_false
                )

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type CREATED_BY
            if "created_by" in item.properties[key]:
                fields.append(
                    {
                        "name": key,
                        "value": item.properties[key].created_by.name,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type CREATED_TIME
            if "created_time" in item.properties[key]:
                # Format the value
                value = transform_datetime(item.properties[key].created_time)

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type DATE
            if "date" in item.properties[key]:
                # Format the value
                value = transform_datetime(item.properties[key].date.start)
                if item.properties[key].date.end is not None:
                    value += " to " + transform_datetime(
                        item.properties[key].date.end
                    )

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type EMAIL
            if "email" in item.properties[key]:
                # Format the value
                value = config.empty_value
                if item.properties[key].email:
                    value = item.properties[key].email

                # Add to fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type UNIQUE_ID
            if "unique_id" in item.properties[key]:
                # Format the value
                value = (
                    item.properties[key].unique_id.prefix
                    + "-"
                    + str(item.properties[key].unique_id.number)
                )

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type LAST_EDITED_BY
            if "last_edited_by" in item.properties[key]:
                fields.append(
                    {
                        "name": key,
                        "value": item.properties[key].last_edited_by.name,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type LAST_EDITED_TIME
            if "last_edited_time" in item.properties[key]:
                # Format the value
                value = transform_datetime(
                    item.properties[key].last_edited_time
                )

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type MULTI_SELECT
            if "multi_select" in item.properties[key]:
                # Format the value
                value = ", ".join(
                    [i["name"] for i in item.properties[key].multi_select]
                )
                if not value:
                    value = config.empty_value

                # Add to fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type NUMBER
            if "number" in item.properties[key]:
                # Format the value
                value = config.empty_value
                if item.properties[key].number:
                    value = item.properties[key].number

                # Add to fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type PHONE_NUMBER
            if "phone_number" in item.properties[key]:
                # Format the value
                value = config.empty_value
                if item.properties[key].phone_number:
                    value = item.properties[key].phone_number

                # Add to fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type SELECT
            if "select" in item.properties[key]:
                # Format the value
                value = config.empty_value
                if item.properties[key].select:
                    value = item.properties[key].select.name

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type STATUS
            if "status" in item.properties[key]:
                fields.append(
                    {
                        "name": key,
                        "value": item.properties[key].status.name,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type RICH_TEXT
            if "rich_text" in item.properties[key]:
                # Format value
                value = config.empty_value
                if item.properties[key].rich_text:
                    value = item.properties[key].rich_text[0]["plain_text"]

                # Add to field list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

            # If the iterated key is of type URL
            if "url" in item.properties[key]:
                # Format the value
                value = config.empty_value
                if item.properties[key].url:
                    value = item.properties[key].url

                # Add to the fields list
                fields.append(
                    {
                        "name": key,
                        "value": value,
                        "inline": config.inline_attributes,
                    }
                )

        # ! DEBUG
        # pprint(fields)

        # Send to channel
        post_to_discord(item_name, "", image=image, fields=fields)
