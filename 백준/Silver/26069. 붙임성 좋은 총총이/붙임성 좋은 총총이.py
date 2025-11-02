import sys
input = sys.stdin.readline

n = int(input())
d = set(['ChongChong'])

for i in range(n):
    a, b = input().split()

    if a in d or b in d:
        d.add(a)
        d.add(b)

print(len(d))