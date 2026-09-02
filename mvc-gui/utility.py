"""
All the utility functions needed to easily complete this
project!

Author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from datetime import datetime


def convert_string_to_datetime(date: str) -> datetime:
    """
    Takes a date in a string format (e.g., `2022-10-05`) and returns a datetime
    object using the format. If the string given is wrong, it throws and error.

    Hint: Search for "python split a string by delimiter"!

    :param date: a string representing the date.
    :return: A datetime object reflecting the date given as a string.
    """
    # TODO: Fix Me!
    dateOfBirth = datetime.strptime(date, "%Y-%m-%d")
    return dateOfBirth
