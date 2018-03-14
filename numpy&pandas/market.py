import numpy as np

a = [0.4,0.6]
b = [[0.8,0.2],[0.1,0.9]]
n = 2

def markrt(a, b):
    c = [0, 0]
    for i in range(0, n):
        for j in range(0, n):
            c[i] += a[j]*b[j][i]

    if round(c[0],4) != round(a[0],4):
        markrt(c, b)

    else:
        print(c)

# markrt(a, b)

j = np.array([[0.8,0.2],[0.1,0.9]]) #b
i = np.array([0.4,0.6]) #a

def market(a,b):
    is_equal = True
    while is_equal:
        temp = a
        a = temp.dot(b)
        for k in range(len(a)):
            if a[k] != temp[k]:
                break
            else:
                is_equal = False
        
    for k in range(len(a)):
        a[k] = round(a[k], 4)

    print(a)
                
market(i, j)