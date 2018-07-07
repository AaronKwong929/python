a = input("a=")
b = input("b=")
if (a > b):
    temp = a
    a = b
    b = temp
    print("exchange a&b:", "a=", a, ",b=", b)
else:
    print("a<b", "a=", a, "b=", b)
