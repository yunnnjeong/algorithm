import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(n):
    line = input().split()
    age = int(line[0])
    name = line[1]
    m.append((age, name))

m.sort(key=lambda x: x[0])

for age, name in m:
    print(age, name)