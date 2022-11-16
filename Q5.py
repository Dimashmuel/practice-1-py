def arr_int(a):
    x = min(a)
    y = sum(a)
    z = max(a)
    return x, y, z


arr = {1, 23, 12, 34, 8, 0, 5}
a1, a2, a3 = arr_int(arr)
print("min: ", a1, "sum: ", a2, "max: ", a3)
