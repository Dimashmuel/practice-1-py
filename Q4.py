def fun():
    arr = []
    while True:
        x = int(input("Enter new number: "))
        if x < 0:
            return arr
        else:
            arr.append(x)


print(fun())


