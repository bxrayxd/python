def calc() -> int:
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = a + b
        return c
    except ValueError:
        print("Please enter numeric values only.")
        return calc()


print(calc())
