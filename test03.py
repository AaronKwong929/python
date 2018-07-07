'''
list=['a','b','c']
list.append(True)#append()只能添加一个内容
print(list)
list.extend([False,'1'])#extend()相当于+号 列表末尾添加另一序列
print(list)
list2=['FUCK','you']
print(list+list2)#等同extend()
'''

score = [68, 75, 32, 99, 78, 45, 888, 72, 83, 78]
a = 0
b = 0
c = 0
d = 0
e = 0
print("成绩分别为：", score)
for i in score:
    if i < 60:
        e += 1
    elif i < 70:
        d += 1
    elif i < 80:
        c += 1
    elif i < 90:
        b += 1
    else:
        a = +1
print("统计结果：", "优：", a, "良：", b, "中：", c, "及格：", d, "差：", e)
'''
s="Python"
print(s)
'''
'''s.replace('h','i')
print(s)'''
'''
li=["apple","peach","orange","banana"]
sep=[","]
s=sep.join(li)
print(s)
sep=[","]
s=sep.join(li)
print(s)
'''
'''
str="123,45"
#list(str)
print(str)
'''
'''
d={"zhou":95,"bob":75,"tracy":85}
print(d["zhou"])
'''
