from datetime import date

def get_shift(month: int, day: int, hour: int) -> str:
    day_number = date(2025, month, day).timetuple().tm_yday

    rotation = (day_number - 1) // 4 + 1
    pairs = ("C", "D") if rotation % 2 == 0 else ("A", "B")

    rem = rotation % 4
    day_group, night_group = pairs[::-1] if rem in (1, 3) else pairs

    return day_group if 7 <= hour < 19 else night_group

group = get_shift(6, 15, 10)
print(f"This is group: {group} shift")
