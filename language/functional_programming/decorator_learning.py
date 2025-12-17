# 在函数执行前打印文字
def decorator1(func):
    print("decorator1")
    return func  # 返回原始函数，使装饰后的函数仍然可调用


# 在函数执行后打印文字，但由于return func，f()会再执行一次，因此需要进行改进
def decorator2(func):
    func()
    print("decorator2")
    return func


def decorator3(func):
    def wrapper():
        func()
        print("decorator3")

    # return wrapper()    # 错误，这样返回的是wrapper()的执行结果
    return wrapper  # 返回wrapper函数本身，而不是调用它


@decorator1
@decorator2
@decorator3
def f():
    print("f")
# 等价于 f = decorator1(decorator2(decorator3(f)))

f()
