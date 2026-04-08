import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append((int(age), i, name))

arr.sort(key=lambda x: x[0])

for age, i, name in arr:
    print(age, name)