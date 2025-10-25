import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    c = input().split()
    
    if c[0] == "push":
        num = int(c[1])
        stack.append(num)
        
    elif c[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif c[0] == "size":
        print(len(stack))
            
    elif c[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
            
    elif c[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)