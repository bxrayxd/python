import calendar
from datetime import datetime


def get_input():
    while True:
        try:
            date = input("Date (yyyy-MM-DD): ")
            year, month, day = map(int, date.split("-"))

            if not (1900 <= year <= 3000):
                raise ValueError("Invalid year")
            if not (1 <= month <= 12):
                raise ValueError("Invalid month")
            if not (1 <= day <= calendar.monthrange(year, month)[1]):
                raise ValueError("Invalid day")
            break

        except ValueError as e:
            print(f"Invalid input. Please use yyyy-MM-DD (Error: {e})")
    while True:
        try:
            time = input("Time (HH:MM)24H: ")
            hour, minute = map(int, time.split(":"))
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Invalid time.")
            break

        except ValueError as e:
            print(f"Invalid input. Please use HH:MM (Error: {e})")

    return year, month, day, hour, minute


def get_shift_rotation(year: int, month: int, day: int):
    current_date = datetime(year, month, day)
    reference_date = datetime(2025, 12, 30)

    days_passed = (current_date - reference_date).days + 1
    rotation = (days_passed - 1) // 4 + 1
    return rotation


def get_shift(rotation: int) -> tuple[str, str]:
    if rotation % 2 == 0:
        first_group, second_group = "C", "D"
    else:
        first_group, second_group = "A", "B"

    remainder = rotation % 4 + 1

    if remainder == 1:
        return first_group, second_group

    if remainder == 2:
        return second_group, first_group

    if remainder == 3:
        return second_group, first_group

    if remainder == 4:
        return first_group, second_group

    else:
        return "wrong", "wrong"


def get_group(hour: int, day_group: str, night_group: str) -> str:
    if 7 <= hour < 19:
        return day_group

    return night_group


def main():
    while True:
        year, month, day, hour, minute = get_input()
        rotation = get_shift_rotation(year, month, day)
        day_group, night_group = get_shift(rotation)
        group = get_group(hour, day_group, night_group)
        print(f"This is group: {group} shift")
        i = input("Press any key to continue, 0 to exit ")
        if i == "0":
            break


if __name__ == "__main__":
    main()
