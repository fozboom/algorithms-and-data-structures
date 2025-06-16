import sys

MIN_VALUE = -sys.maxsize - 1

n = int(input())

max_sum = MIN_VALUE
curr_sum = MIN_VALUE
arr = list(map(int, input().split()))

for el in arr:
    curr_sum = max(el, curr_sum + el)
    max_sum = max(curr_sum, max_sum)

print(max_sum)
