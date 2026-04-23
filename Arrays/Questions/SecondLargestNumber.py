# Approach 1
nums = [1, 2, 3, 4, 5]

n = len(nums)

first_largest = float('-inf')
second_largest = float('-inf')

for i in range(0, n):

    if (nums[i] > first_largest):
        first_largest = nums[i]

print(f"First largest number in {nums}: {first_largest}")


for j in range(0, n):

    if (nums[j] > second_largest) & (nums[j] != first_largest):
        second_largest = nums[j]

print(f"Second largest number in {nums} : {second_largest}")