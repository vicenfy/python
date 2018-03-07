#day 5

#基本属性
import numpy as np

array = np.array([[1,2,3],[2,3,4]])

print(array)
print('number of dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)

#创建数组
a = np.array([2,23,4], dtype=np.int32) #float(32)
print(a.dtype)

b = np.array([[2,23,4],
              [2,32,4]])
print(b)

c = np.zeros((3,4)) #3行4列数列 #ones((3,4)) #empty
print(c)

d = np.arange(10, 20, 2)
print(d)

e = np.arange(12).reshape((3,4))
print(e)

f = np.linspace(1, 10, 6).reshape((2,3))
print(f)