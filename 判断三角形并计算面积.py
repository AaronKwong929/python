import math
a = input("输入三角形的第一条边：")
b = input("输入三角形的第二条边：")
c = input("输入三角形的第三条边：")
a = float(a)
b = float(b)
c = float(c)
if a <= 0 or b <= 0 or c <= 0:
    print("数据输入错误,不构成三角形。")
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("不构成三角形.")
else:
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    if a == b and b == c:
        print("这是一个等边三角形,面积为：" + str(area))
    if (a == b and a!=c) or (a == c and a!=b)or (b == c and b!=a):
        print("这是一个等腰三角形,面积为：" + str(area))
    if a**2 + b**2 == c**2:
        print("这是一个直角三角形,面积为：" + str(area))
    else:
        print("这是一个普通三角形,面积为：" + str(area))
