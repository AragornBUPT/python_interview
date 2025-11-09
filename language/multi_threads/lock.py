import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if lock.acquire(1):
            num = num + 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            lock.acquire()
            lock.release()
            lock.release()


class SimpleThread(threading.Thread):
    def run(self) -> None:
        global num

        lock.acquire()
        # lock.acquire()  # 多次尝试获取锁会卡死
        num += 1
        print(num)
        lock.release()
        # lock.release()  # 重复释放锁，会报错，抛异常


num = 0
lock = threading.Lock()


def test():
    for i in range(5):
        t = MyThread()
        t.start()


def test_simple():
    for i in range(5):
        t = SimpleThread()
        t.start()


if __name__ == "__main__":
    # test()
    test_simple()
