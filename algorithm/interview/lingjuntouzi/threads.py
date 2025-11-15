import threading
import time


def show1():
    for i in range(1, 9, 3):
        lock_show2.acquire()
        print(i, end="")
        print(i + 1, end="")
        print(i + 2, end="")
        time.sleep(0.2)
        lock_show1.release()


def show2():
    for i in range(26):
        lock_show1.acquire()
        print(chr(i + ord("A")))
        time.sleep(0.2)
        lock_show2.release()


lock_show1 = threading.Lock()
lock_show2 = threading.Lock()
show1_thread = threading.Thread(target=show1)
show2_thread = threading.Thread(target=show2)
lock_show1.acquire()
show1_thread.start()
show2_thread.start()
