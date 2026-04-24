"""
Question : Count the number of unique elements in an Array

"""

class Solution(object):

    def check(self, nums):

        n = len(nums)
        empty_dict = {}

        for i in range(0, n):
            empty_dict[nums[i]] = 0

        j = 0
        for key in empty_dict:
            nums[j] = key
            j += 1

        return j
    
solution = Solution()
print(solution.check([1, 1, 2, 2, 3, 3, 4, 4]))