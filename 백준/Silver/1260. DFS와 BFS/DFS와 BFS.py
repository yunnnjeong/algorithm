from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_v in graph[current]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True

visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)