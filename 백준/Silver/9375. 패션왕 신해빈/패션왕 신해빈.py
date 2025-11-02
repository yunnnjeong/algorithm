import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    clothes = {}

    for i in range(n):
        name, kind = input().split()

        if kind in clothes:
            clothes[kind] += 1

        else:
            clothes[kind] = 1

    answer = 1
    for count in clothes.values():
        answer *= (count + 1)  

    answer -= 1
    print(answer)