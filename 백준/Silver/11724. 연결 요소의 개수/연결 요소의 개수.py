import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)