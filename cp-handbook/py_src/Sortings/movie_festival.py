import sys

input = sys.stdin.readline

n = int(input())


movies: list[tuple[int, int]] = []
for _ in range(n):
    start, end = map(int, input().split())
    movies.append((start, end))

movies.sort(key=lambda x: x[1])

count = 0

curr_end_time = 0

for start, end in movies:
    if start >= curr_end_time:
        count += 1
        curr_end_time = end

print(count)
