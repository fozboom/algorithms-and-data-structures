import bisect
import sys

input = sys.stdin.readline
n = int(input())

towers_tops = []

for kube_size in map(int, input().split()):
    idx = bisect.bisect_right(towers_tops, kube_size)

    if idx < len(towers_tops):
        towers_tops[idx] = kube_size
    else:
        towers_tops.append(kube_size)

print(len(towers_tops))