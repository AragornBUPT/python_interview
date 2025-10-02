# https://cloud.tencent.com/developer/article/2045561?pos=comment
import sys


class A:

    def __init__(self):
        pass


print("创建对象 0 + 1 =", sys.getrefcount(A()))

a = A()
print("创建对象并赋值 0 + 2 =", sys.getrefcount(a))

b = a
c = a
print("赋给2个变量 2 + 2 =", sys.getrefcount(a))

b = None
print("变量重新赋值 4 - 1 =", sys.getrefcount(a))

del c
print("del对象 3 - 1 =", sys.getrefcount(a))

d = [a, a, a]
print("3次加入列表 2 + 3 =", sys.getrefcount(a))


def func(c):
    print("传入函数 1 + 2 = ", sys.getrefcount(c))


func(A())
