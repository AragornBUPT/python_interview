import random
import sys
import os

# 添加项目根目录到sys.path以便绝对导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sort.quick_sort import quick_sort

if __name__ == "__main__":
    arr_35 = list(range(1, 36))
    first_arr = []
    for i in range(5):
        n = random.choice(arr_35)
        first_arr.append(n)
        print(n)
        # arr_35.remove(n)

    quick_sort(first_arr, 0, len(first_arr) - 1)

    arr_12 = list(range(1, 13))
    second_arr = []
    for i in range(2):
        n = random.randint(1, 12)
        second_arr.append(n)
        print(n)
        # arr_12.remove(n)

    quick_sort(second_arr, 0, len(second_arr) - 1)

    print(first_arr, second_arr)
