"""
Given an array of n numbers, our task is to calculate the maximum subarray sum, i.e., the largest possible sum of a sequence of consecutive values in the array. We assume that an empty subarray is allowed, so the maximum subarray
sum is always at least 0.
"""

from typing import List


# O(n) complexity
def solve(arr: List[int]):
    cur_sum = 0
    best_sum = 0

    for i in range(len(arr)):
        # if the next sum less than just next element, then start a new sum from the next element
        # otherwise, continue the sum
        cur_sum = max(cur_sum + arr[i], arr[i])
        best_sum = max(best_sum, cur_sum)

    print(best_sum)
    return best_sum


def test_solve():
    assert solve([-1, -4, 6, -3, 12, -1, 7]) == 21
    assert solve([-1, -4, 6, -3, 12, -15, 7]) == 15
    assert solve([-2, -3, -1, -4]) == 0
    assert solve([-2, -3, -1, -4, 10]) == 10
    assert solve([-2, -3, -1, -4, 10, -10]) == 10


if __name__ == "__main__":
    test_solve()
