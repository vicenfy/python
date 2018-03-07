def add(a,b):
    c = a+b
    print(c)

add(1,2)

APPLE = 100
a = None

def fun():
    global a #改变a为全局变量
    a = 20
    return a+100

print(APPLE)
print('a past=', a)
print(fun())
print('a now=', a)