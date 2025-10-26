import sys
input = sys.stdin.readline

def check(s):
    a = []
    for c in s:
        if c == '(' or c == '[':
            a.append(c)
        elif c == ')':
            if not a or a[-1] != '(':
                return "no"
            a.pop()
        elif c == ']':
            if not a or a[-1] != '[':
                return "no"
            a.pop()
    return "yes" if not a else "no"

while True:
    s = input().rstrip()
    if s == '.':
        break
    print(check(s))