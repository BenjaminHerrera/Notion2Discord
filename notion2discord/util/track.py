# Import
from typing import Union
import json
import os


def set_tracker_var(key: str, value: str) -> None:
    """Sets a persistent tracking value into the .n2d_track file

    Args:
        key (str): Name of the variable
        value (str): Value of the variable
    """
    # Expand the user's home directory
    file_path = os.path.expanduser("~/.n2d_track")

    # Create a placeholder variable
    data = {}

    # Check if the file exists and read the existing data if it does
    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        with open(file_path, "r") as file:
            data = json.load(file)

    # Update the data with the new key-value pair
    data[key] = value

    # Write to the file
    with open(file_path, "w+") as file:
        json.dump(data, file)


def get_tracker_var(key: str) -> Union[None, str]:
    """Get a persistent tracking value from the .n2d_track file

    Args:
        key (str): Name of the variable
    """
    # Expand the user's home directory
    file_path = os.path.expanduser("~/.n2d_track")

    # Check if the file exists
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None

    # Return the contents of the file
    with open(file_path, "r") as file:
        return json.load(file)[key]
