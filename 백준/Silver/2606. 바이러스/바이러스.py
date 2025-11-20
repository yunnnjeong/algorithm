n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(computer):
    visited[computer] = True
    count = 1
    
    for next in graph[computer]:
        if not visited[next]:
            count += dfs(next)
    
    return count

result = dfs(1)
print(result - 1)