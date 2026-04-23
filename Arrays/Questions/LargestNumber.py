# approach 1
nums = [1, 2, 3, 4, 5]

n = len(nums)
largest = float('-inf')


for i in range(0, n):

    if nums[i] > largest:
        largest = nums[i]

print(largest)
