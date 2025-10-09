n = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
cumulative = 0

for time in times:
    cumulative += time
    total += cumulative

print(total)