import math
a = input("输入三角形的第一条边：")
b = input("输入三角形的第二条边：")
c = input("输入三角形的第三条边：")
a = float(a)
b = float(b)
c = float(c)
if a <= 0 or b <= 0 or c <= 0:
    print("数据输入错误,不构成三角形。")
else:
    if a > b:
        t = a
        a = b
        b = t
    if a > c:
        t = a
        a = c
        c = t
    if b > c:
        t = b
        b = c
        c = t
    if a+b > c and a+c > b and b+c > a:
        print("构成三角形。")
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    if a == b and b == c:
        print("这是一个等边三角形。")
    elif a == b or a == c or b == c:
        print("这是一个等腰三角形")
    elif a**2 + b**2 == c**2:
        print("这是一个直角三角形")
    else:
        print("这是一个普通三角形")
        print("三角形的面积为：", area)

