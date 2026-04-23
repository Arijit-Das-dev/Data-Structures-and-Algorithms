nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(nums)

for i in range(0, n):

    max_num = i

    for j in range(i+1, n):

        if nums[j] > nums[max_num]:

            max_num = j

    temp = nums[i]
    nums[i] = nums[max_num]
    nums[max_num] = temp

print(nums)