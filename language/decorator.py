import datetime
import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"{fn.__name__} execute at {datetime.datetime.now()}")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} finish at {datetime.datetime.now()}")
        return result

    return wrapper


# def metric(fn):
#     print("%s executed in %s ms" % (fn.__name__, 10.24))
#     return fn


# 测试
@metric
def fast(x, y):
    print("fast")
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    print("slow")
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print("测试失败!")
elif s != 7986:
    print("测试失败!")
