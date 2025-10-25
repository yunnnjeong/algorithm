import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
result = []
tag = False

for char in s:
    if char == '<':
        while stack:
            result.append(stack.pop())
        tag = True
        result.append(char)
    
    elif char == '>':
        tag = False
        result.append(char)
    
    elif tag:
        result.append(char)
    
    elif char == ' ':
        while stack:
            result.append(stack.pop())
        result.append(char)
    
    else:
        stack.append(char)

while stack:
    result.append(stack.pop())

print(''.join(result))