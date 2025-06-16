n, target = map(int, input().split())

arr = list((value, index) for index, value in enumerate(map(int, input().split()), 1))

arr.sort()

left = 0
right = len(arr) - 1

while left < right:
    if (arr[left][0] + arr[right][0]) == target:
        print(arr[left][1], arr[right][1])
        break
    elif arr[left][0] + arr[right][0] < target:
        left += 1
    else:
        right -= 1
else:
    print('IMPOSSIBLE')
