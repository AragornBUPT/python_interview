import msvcrt
import sys
import threading
import time


is_running = True


def print_num(mod: int):
    num = 0

    global is_running
    while True:
        if is_running:
            num = num % mod
            num += 1
            print(f"\r{num:02d}", end="", flush=True)
            # sys.stdout.write(f"\r{num:02d}")
            # sys.stdout.flush()
            # print(f"{num:02d}")
        else:
            time.sleep(1)


def print_pause():
    global is_running
    while True:
        if msvcrt.getch():
            is_running = not is_running
            print()


if __name__ == "__main__":
    print_thread = threading.Thread(target=print_num, args=(12,))
    print_thread.start()

    print_pause()
