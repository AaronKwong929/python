'''#单一排
for i in range(0,10):
  j=1
  print(i,"*",j,"=",i*j)'''
# 全表
for i in range(1, 10, 1):
    for j in range(1, i + 1, 1):
        print(i, "*", j, "=", i * j, end="   ")
    print("\n\n")