PI = 3.1415926535
r = input("请输入圆/球的半径：")
r = float(r)
while r <= 0:  # if r.isdigit():
    print("输入数据错误，请重新输入。")
    r = input("请输入圆/球的半径：")
    r = float(r)
s = PI * r**2
v = (4 * PI * r**3) / 3
print("圆的面积为：%.4f" % s)  # 输出位数 "xxxxx%.nf"%s
print("球的体积为：%.4f" % v)