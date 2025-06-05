from typing import List


def bubble_sort(arr: List[int]):
    size = len(arr)

    for i in range(size):
        sorted = True
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break
    print(arr)
    return arr


def test_bubble_sort():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    test_bubble_sort()
