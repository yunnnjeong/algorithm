n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)

m = 0
for i in range(n):
    w = r[i] * (i + 1)
    m = max(m, w)

print(m)