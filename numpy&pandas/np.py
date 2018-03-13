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
#基础计算
g = np.array([10,20,30,40])
h = g**2
print(h<=400)
#点乘
i = np.array([[0.8,0.2],[0.1,0.9]])
j = np.array([0.4,0.6])
k = np.dot(j, i)
print(j.dot(i))
#随机数
a = np.random.random((2,4))
print(a)
print(a.sum(axis=1)) #axis=1行 0列
print(a.min(axis=0)) #每列的最小数
print(a.max(axis=1)) #每行的最大数
# print(a.mean()) #平均值
#特殊
a = np.arange(14,2,-1).reshape(3,4)
print(a)
print(a.argmax()) #最大索引
print(a.argmin())
print(a.mean()) #平均值
print(np.median(a))#中位数
print(a.cumsum()) #累加
print(np.diff(a)) #累差
print(a.nonzero()) #两个array，分别表示行和列的index
print(np.sort(a)) #每行的排序
print((a.T).dot(a)) #转置
print(a.clip(5,9)) #小于5的数变为5，大于9的数变为9，其他不变