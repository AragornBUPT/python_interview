def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = create_counter()
c2 = create_counter()
print(c1(), c1(), c2())

# https://cloud.tencent.com/developer/article/2332412
b = 6


def f1(a):
    print(a)
    print(b)


f1(1)

b = 6


def f2(a):
    print(a)
    print(b)
    b = 2


f2(1)
