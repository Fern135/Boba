from datetime import datetime, timedelta

def get_current_date_MM_DD_YYYY() -> str:
    """
    Get the current date in MM:DD:YYYY format.

    Returns:
        str: The current date in MM:DD:YYYY format.

    Example:
        current_date = get_current_date_MM_DD_YYYY()
        print(current_date)  # Output: "07:18:2023"
    """
    return datetime.now().strftime("%m:%d:%Y")

def get_current_date_with_full_month() -> str:
    """
        Get the current date with the full name of the month in MM:DD:YYYY format.

        Returns:
            str: The current date with the full name of the month in MM:DD:YYYY format.

        Example:
            current_date = get_current_date_with_full_month()
            print(current_date)  # Output: "July 18, 2023"
    """
    return datetime.now().strftime("%B %d, %Y")

def get_current_date() -> datetime:
    """
    Get the current date and time.

    Returns:
        datetime: The current date and time.

    Example:
        current_date = get_current_date()
        print(current_date)
    """
    return datetime.now()

def get_current_time_24() -> str:
    """
        Get the current time in 24-hour format.

        Returns:
            str: The current time in 24-hour format.

        Example:
            current_time = get_current_time_24()
            print(current_time)  # Output: "13:30"
    """
    return datetime.now().strftime("%H:%M")

def get_current_time_12() -> str:
    """
        Get the current time in 12-hour format (AM/PM).

        Returns:
            str: The current time in 12-hour format.

        Example:
            current_time = get_current_time_12()
            print(current_time)  # Output: "01:30 PM"
    """
    return datetime.now().strftime("%I:%M %p")
    

def get_formatted_date(date: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
        Format a given datetime object into a string using the specified format.

        Parameters:
            date (datetime): The datetime object to be formatted.
            format_str (str): The format string to be used for formatting. Default is "%Y-%m-%d %H:%M:%S".

        Returns:
            str: The formatted date as a string.

        Example:
            current_date = get_current_date()
            formatted_date = get_formatted_date(current_date, "%Y-%m-%d")
            print(formatted_date)
    """
    return date.strftime(format_str)


def parse_date(date_string: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
        Parse a date string into a datetime object using the specified format.

        Parameters:
            date_string (str): The date string to be parsed.
            format_str (str): The format string used in the date string. Default is "%Y-%m-%d %H:%M:%S".

        Returns:
            datetime: The parsed datetime object.

        Example:
            date_str = "2023-07-31 12:30:00"
            parsed_date = parse_date(date_str, "%Y-%m-%d %H:%M:%S")
            print(parsed_date)
    """
    return datetime.strptime(date_string, format_str)


def add_days_to_date(date: datetime, days: int) -> datetime:
    """
        Add a specified number of days to a given date.

        Parameters:
            date (datetime): The date to which days will be added.
            days (int): The number of days to add.

        Returns:
            datetime: The new date after adding days.

        Example:
            current_date = get_current_date()
            new_date = add_days_to_date(current_date, 5)
            print(new_date)
    """
    return date + timedelta(days=days)


def difference_between_dates(start_date: datetime, end_date: datetime) -> timedelta:
    """
        Calculate the difference between two dates.

        Parameters:
            start_date (datetime): The start date.
            end_date (datetime): The end date.

        Returns:
            timedelta: The time duration between the two dates.

        Example:
            start_date = parse_date("2023-07-31", "%Y-%m-%d")
            end_date = parse_date("2023-08-05", "%Y-%m-%d")
            duration = difference_between_dates(start_date, end_date)
            print(duration.days)  # Output: 5
    """
    return end_date - start_date
