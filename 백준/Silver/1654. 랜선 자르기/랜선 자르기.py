import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

def count(length):
    total = 0
    for line in lines:
        total += line // length
    return total

left = 1
right = max(lines)
result = 0

while left <= right:
    mid = (left + right) // 2

    if count(mid) >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)