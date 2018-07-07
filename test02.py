'''i=1
sum=0
sum+=i;i+=1
sum+=i;i+=1
sum+=i;i+=1
sum+=i;i+=1
sum+=i;i+=1
print(sum)
'''
'''
i=1
sum=0
while i<=100:
  sum+=i
  i+=2
print(sum)
'''
'''
total=0
counter=1
while counter<=5:
  total=total+int(input("输入一个数字："))
  counter+=1
print("平均值为：%.2f"%(float(total)/5))
'''
'''
a=1
b=1
c=1
PI=0
while abs(b)>0.00001:
  PI+=b
  a+=2
  c=-c
  b=c/a
PI=PI*4
print(PI)
'''
'''
a=0
i=1
s=0
n=int(input("请输入n："))
while i<=n:
  a=a+i
  i+=1
  t=1/a
  s=s+t
print("s=",s)
'''
'''
sum=0
count=0
x=float(input("输入一个数字：（输入0则退出）"))
if x==0:
  print("结束。")
else:
  while x!=0:
    sum=sum+x
    count+=1
    x=float(input("输入一个数字：（输入0则退出）"))
  print("总个数为：",count,"平均分为：",sum/count)
'''
'''
print("200以内可以被17整除的数：")
for i in range(1,201,1):
  if i%17!=0:
    continue
  print (i,end=" ")
'''
'''
number=10
running=True
while running:
  guess=int(input("请输入一个数字："))
  if guess<number:
    print("比正确值要小，请重新输入：")
  elif guess>number:
    print("比正确值要大，请重新输入：")
  else:
    print("猜对了。")
    running=False
print("结束。")
'''
'''
score=[97,99,98,98,96,100]
print("分数为：",score)
print("平均分为：",sum(score)/len(score))
'''
'''
score=[97,99,98,98,96,100]
print("分数为：",score)
a=0
for i in score:
  a+=i
print(a/len(score))
'''
'''
score=[97,99,98,98,96,100]
print("分数为：",score)
a=0
for i in range(6):
  a+=score[i]
print(a/len(score))
'''
'''
i=2
sum=0
while True:
  sum+=i
  if sum>100:
    break
  else:
    i+=2
print(i)
'''
'''
i=2;sum=0
while sum<100:
  i+=2
  sum+=i
print(i)
'''
'''
for i in range(0,5):
  print("$",end=" ")
print()
print()



for i in range(0,3):
  for j in range(0,5):
    print("*",end=" ")
  print()
'''
'''
for i in range(1,4):
  for j in range(0,2*i-1):
    print("*",end=" ")
  print()
'''
for i in range(1, 4):
    for j in range(0, 3 - i):
        print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("$", end=" ")
    print()
