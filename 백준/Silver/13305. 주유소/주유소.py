n = int(input())

d = []
inp = input().split()
for i in range(n - 1):
    d.append(int(inp[i]))

p = []
inp = input().split()
for i in range(n):
    p.append(int(inp[i]))

t = 0
m = p[0]

for i in range(n - 1):
    if p[i] < m:
        m = p[i]
    
    t = t + (m * d[i])

print(t)