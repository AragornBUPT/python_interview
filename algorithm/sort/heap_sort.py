"""
构造小顶堆
"""


def heapify(arr: [int], parent: int, last_index: int):
    left = 2 * parent + 1
    right = 2 * parent + 2

    min = parent
    if left <= last_index and arr[left] < arr[min]:
        min = left

    if right <= last_index and arr[right] < arr[min]:
        min = right

    if min != parent:
        arr[min], arr[parent] = arr[parent], arr[min]
        heapify(arr=arr, parent=min, last_index=last_index)


def buildHeap(arr: [int], last_index: int):
    parent = (last_index - 1) // 2
    while parent >= 0:
        heapify(arr=arr, parent=parent, last_index=last_index)
        parent -= 1


def heapSort(arr: [int]):
    last_index = len(arr) - 1
    while last_index >= 0:
        buildHeap(arr=arr, last_index=last_index)
        arr[0], arr[last_index] = arr[last_index], arr[0]
        last_index -= 1


if __name__ == "__main__":
    arr = [63, 23, 4234, 11, 109, 999, 333, 234]
    print(arr)

    buildHeap(arr=arr, last_index=len(arr) - 1)
    print(arr)

    arr = [63, 23, 4234, 11, 109, 999, 333, 234]
    print(arr)

    heapSort(arr=arr)
    print(arr)
