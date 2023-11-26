# Imports
from config.config import config
from datetime import datetime


def transform_datetime(input_str: str) -> str:
    """Turns a given datetime string into `DD MM YYYY @ hh:mm` format

    Args:
        input_str (_type_): datetime string to convert

    Returns:
        str: Formatted datetime string
    """

    # Check if the string includes time and timezone information
    if "T" in input_str and "-" in input_str and len(input_str) > 10:
        format_str = "%Y-%m-%dT%H:%M:%S.%f%z"
    elif len(input_str) == 10:
        format_str = "%Y-%m-%d"

    # Parse using the determined format
    dt = datetime.strptime(input_str, format_str)

    # Format the datetime object into the desired string format
    if format_str == "%Y-%m-%dT%H:%M:%S.%f%z":
        result = dt.strftime(config.datetime_format_with_time)
    else:
        result = dt.strftime(config.datetime_format_without_time)
    return result
