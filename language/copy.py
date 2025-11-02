obj = ["name", ["age", 18]]

a = obj[:]
b = list(obj)


def print_all():
    print(f"obj : {obj}")
    print(f"a : {a}")
    print(f"b : {b}")
    print()


print_all()

a[0] = "lisa"
b[0] = "zhangsan"
print_all()

a[1][1] = 25
print_all()
