
def new_number(c):
    c = c.replace('.', '')
    result = "".join(dict.fromkeys(c))
    return result


x = input('Enter float number: ')
print(new_number(x))
