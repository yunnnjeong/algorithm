nums = []
for i in range(9):
    nums.append(int(input()))

mx = max(nums)
idx = nums.index(mx) + 1

print(mx)
print(idx)