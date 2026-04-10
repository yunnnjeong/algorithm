import sys
input = sys.stdin.readline

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
targets = list(map(int, input().split()))

result = []
for target in targets:
    result.append(binary_search(arr, target))

print('\n'.join(map(str, result)))