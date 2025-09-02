import sys

input = sys.stdin.readline

n = int(input())

k = list(map(int, input().split()))

left = 0
map_id_index = {}
max_length = 0
for right in range(n):
    curr = k[right]

    if curr in map_id_index and map_id_index[curr] >= left:
        left = map_id_index[curr] + 1

    map_id_index[curr] = right
    max_length = max(max_length, right - left + 1)

print(max_length)
