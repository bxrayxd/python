DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
def get_input():
    while True:
        try:
            date = input("Date (MM-DD): ")
            time = input("Time (HH:MM)24H: ")
            month, day = map(int, date.split("-"))
            hour, minute = map(int, time.split(":"))

            if not (1 <= month <= 12):
                raise ValueError("Invalid month")
            if not (1 <= day <= DAYS_IN_MONTH[month - 1]):
                raise ValueError("Invalid day")
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Invalid time.")

            return month, day, hour, minute

        except ValueError as e:
            print(f"Invalid input. Please use MM-DD and HH:MM (Error: {e})")

def get_day_number(month: int, day: int):
    days_before_month = 0
    for i in range(month - 1):
        days_before_month += DAYS_IN_MONTH[i]
    return days_before_month + day

def get_shift_rotation(day_number: int):
    return (day_number - 1) // 4 + 1

def get_which_groups(rotation: int) -> tuple[str, str]:
    if rotation % 2 == 0:
        return "C", "D"
    else:
        return "A", "B"

def get_shift(rotation: int) -> tuple[str, str]:
    first_group, second_group = get_which_groups(rotation)
    remainder = rotation % 4
    if remainder == 1:
        return second_group, first_group

    elif remainder == 2:
        return first_group, second_group

    elif remainder == 3:
        return second_group, first_group

    else:
        return first_group, second_group

def get_group(hour: int, day_group: str, night_group: str) -> str:
    if 7 <= hour < 19:
        return day_group

    return night_group

def main():
    month, day, hour, minute = get_input()
    day_number = get_day_number(month, day)
    rotation = get_shift_rotation(day_number)
    day_group, night_group = get_shift(rotation)
    group = get_group(hour, day_group, night_group)
    print(f"This is group: {group} shift")

if __name__ == "__main__":
    main()
