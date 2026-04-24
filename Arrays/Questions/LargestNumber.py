"""
Question : Largest Number in an Array of integers.

"""

class Solution(object):

    def largestNumber(self, nums):

        n = len(nums)
        largest = float('-inf')

        for i in range(0, n):

            if (nums[i]>largest):
                largest = nums[i]

        return largest
    
s = Solution()
print(s.largestNumber(nums = [52, -1, 100, 150, 1200, -120.0]))