fname = input("enter your first name: ")
lname = input("enter your last name: ")

welcome = f"welcome: {fname} {lname}"
print(welcome)

print(f"first letter of the first name is: {fname[0]}")
print(f"last letter of the first name is: {fname[-1]}")

firt_name = fname.capitalize()
last_name = lname.capitalize()
print(firt_name, last_name)

has_o_first = "o" in fname.lower()
has_o_last = "o" in lname.lower()
print("does the first and last name have o ?", {has_o_first}, {has_o_last})

print("first name without the frist and last letter", {fname[1:-1]})
print("first name without the frist and last letter", {lname[1:-1]})

new_fname = fname[:-2] + fname[-2] * 3 + fname[-1] * 3
new_lname = lname[:-2] + lname[-2] * 3 + lname[-1] * 3
print(new_fname, " ", new_lname)
