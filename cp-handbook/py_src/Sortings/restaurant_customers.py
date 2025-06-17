import sys

input = sys.stdin.readline

n = int(input())

events: list[tuple[int, int]] = []

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a, 1))
    events.append((b + 1, -1))

events.sort()

current = max_customers = 0
for _, change in events:
    current += change
    if current > max_customers:
        max_customers = current

print(max_customers)
