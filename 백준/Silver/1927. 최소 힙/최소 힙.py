import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, x)