import sys
input = sys.stdin.readline

def check(s):
    a = []
    for c in s:
        if c == '(':
            a.append(c)
        elif c == ')':
            if not a:
                return "NO"
            a.pop()
    return "YES" if not a else "NO"

n = int(input())
for _ in range(n):
    s = input().strip()
    print(check(s))