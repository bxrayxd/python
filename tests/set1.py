def addone(x: int):
    return x + 1


t1 = {100, 200, 300}

res = map(addone, t1)
print(list(res))
print(t1)
