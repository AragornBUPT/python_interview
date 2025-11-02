def partition(arr, left, right):
    flag = arr[left]
    last_ptr = right + 1  # last_ptr为>flag的最小的索引

    i = left + 1
    while True:
        if i == last_ptr:
            break

        if arr[i] > flag:
            last_ptr -= 1
            arr[i], arr[last_ptr] = arr[last_ptr], arr[i]

            continue

        i += 1

    last_ptr -= 1
    arr[last_ptr], arr[left] = arr[left], arr[last_ptr]

    return last_ptr


def quick_sort(arr, left, right):
    print(f"left : {left}, right : {right}")
    if left >= right:
        return

    flag = partition(arr=arr, left=left, right=right)
    quick_sort(arr=arr, left=left, right=flag - 1)
    quick_sort(arr=arr, left=flag + 1, right=right)


if __name__ == "__main__":
    ori_array = [81,94,87,78,87,83,75,66,86,82,93,88]
    length = len(ori_array)
    print(f"length of ori_array : {length}")

    quick_sort(ori_array, 0, length - 1)
    print(ori_array)
