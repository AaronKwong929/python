import numpy as np
'''
array1 = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.int)  # dtype参数设置数组类型 int(默认32)，int64,float,float64
print(array1)
print(array1.ndim)  # 输出矩阵维度
print(array1.shape)  # 几行几列
print(array1.size)  # 几个元素
print(array1.dtype)  #数组类型
'''
'''
array2 = np.zeros((3, 4)) # x行y列矩阵 , np.ones 全为1, empty((接近0的))
print(array2)
'''
'''
arange1 = np.arange(0, 20)  #数列，(10, 20, 2)步长,(10) 从0-9
# .reshape((4, 5))  #变为四行五列矩阵
print(arange1)
'''
'''
line1 = np.linspace(1, 10, 3)  # 第三个参数为等距离分段段数
print(line1)
'''

'''
array3 = np.array([10, 20, 30, 40])
array4 = np.array([4, 3, 2, 1])
print(array3, array4)
add = array3 + array4
sub = array3 - array4
mul = array3 * array4
div = array3 / array4
matrix_mul = np.dot(array3, array4)  # 矩阵点乘
# 或： matrix_mul = array3.dot(array4)
print(matrix_mul)
# print(add, sub, mul, div)
# square = array3**2
# cube = array3**3
# print(square, cube)
# print(array4 < 3)  矩阵内小于3的元素判断，返回boolean列表
'''
'''
np.min(array3 ,axis=1)  #求其中最小 axis 1为行  0为列
np.max()
np.sum()