import sys
input = sys.stdin.readline
n, c = map(int, input().split())
numbers = list(map(int, input().split()))
b = {}
first = {}

idx = 0
for num in numbers:

    if num in b:
        b[num] += 1
    else:
        b[num] = 1
    
    if num not in first:
        first[num] = idx
    
    idx += 1

sort_list = []
for num in b:
    sort_list.append((-b[num], first[num], num))
sort_list.sort()

result = []
for data in sort_list:
    num = data[2]
    count = b[num]
    for i in range(count):
        result.append(num)
print(*result)