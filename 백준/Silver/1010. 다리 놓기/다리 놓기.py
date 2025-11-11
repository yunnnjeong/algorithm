count = int(input())

for _ in range(count):
    west, east = map(int, input().split())
    
    result = 1
    
    for i in range(west):
        result = result * (east - i) // (i + 1)
    
    print(result)