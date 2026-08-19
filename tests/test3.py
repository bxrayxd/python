def get_grade_label(score: int) -> str:
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score <= 95:
        return "A"
    elif score <= 100:
        return "A+"
    else:
        return "Invalid"


grade = int(input("enter your grade: "))
print(get_grade_label(grade))
