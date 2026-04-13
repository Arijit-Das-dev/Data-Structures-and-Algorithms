nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
freq = {}

for i in range(0, len(nums)):
    if nums[i] not in freq:
        freq[nums[i]] = 1
    else:
        freq[nums[i]] += 1

print(freq)