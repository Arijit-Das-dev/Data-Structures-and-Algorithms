# approach 1
nums = [1, 2, 3, 4, 5]

n = len(nums)
largest = float('-inf')


for i in range(0, n):

    if (nums[i] > largest):
        largest = nums[i]

print(largest)

# approach 2
nums = [1, 2, 3, 4, 5]

n = len(nums)
largest_num = nums[0]

for i in range(1, n):

    if (nums[i] > largest_num):
        largest_num = nums[i]

print(largest_num)