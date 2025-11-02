import random
from algorithm.sort.quick_sort import quick_sort


def lottery():
    print("lottery is running...")
    arr_35 = list(range(1, 36))
    first_arr = []
    for i in range(5):
        n = random.choice(arr_35)
        first_arr.append(n)
        # print(n)
        arr_35.remove(n)

    quick_sort(first_arr, 0, len(first_arr) - 1)

    arr_12 = list(range(1, 13))
    second_arr = []
    for i in range(2):
        n = random.choice(arr_12)
        second_arr.append(n)
        # print(n)
        arr_12.remove(n)

    quick_sort(second_arr, 0, len(second_arr) - 1)

    first_arr_str = " ".join(str(i).zfill(2) for i in first_arr)
    second_arr_str = " ".join(str(i).zfill(2) for i in second_arr)
    print(f"{first_arr_str}   {second_arr_str}")
