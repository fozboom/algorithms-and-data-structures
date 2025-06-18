n = int(input())

sticks = list(map(int, input().split()))

sticks.sort()

target_len = sticks[(len(sticks) - 1) // 2]

res = 0
for stick in sticks:
    res += abs(target_len - stick)

print(res)
