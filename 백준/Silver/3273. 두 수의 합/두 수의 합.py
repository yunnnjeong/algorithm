n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

num_set = set(numbers)
count = 0

for num in numbers:
    if x - num in num_set:
        count += 1

print(count // 2)