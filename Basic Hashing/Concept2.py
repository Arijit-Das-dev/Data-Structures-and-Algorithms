nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
freq = {}

for i in nums:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)