n, x = map(int, input().split())

p = list(map(int, input().split()))

p.sort()
# print(p)
count = 0

i = 0
j = len(p) - 1

while i < j:
    if p[i] + p[j] <= x:
        count += 1
        i += 1
        j -= 1
    else:
        count += 1
        j -= 1
        
if i == j:
    count += 1
    
print(count)