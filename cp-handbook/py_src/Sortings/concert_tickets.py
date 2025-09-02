import sys


def bisect_right(arr: list[int], val: int):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= val:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())

    prices = sorted(list(map(int, input().split())))

    for max_price in map(int, input().split()):
        idx = bisect_right(prices, max_price)

        if idx == 0:
            print(-1)
        else:
            print(prices[idx - 1])

            _ = prices.pop(idx - 1)
