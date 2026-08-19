d1 = {"a": 5, "b": 8, "c": 9}
d2 = {"a": 7, "b": 6, "c": 4}

d3 = {key: max(d1[key], d2[key]) for key in d1}
print(d3)
