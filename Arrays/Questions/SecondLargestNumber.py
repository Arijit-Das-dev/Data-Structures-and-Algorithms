"""
Question : First and Second largest number in an array

"""

class Solution(object):

    def firstAndSecondLargestNumber(self, nums):

        n = len(nums)
        first_largest = float('-inf')
        second_largest = float('-inf')

        for i in range(0, n):

            if (nums[i]>first_largest):
                first_largest = nums[i]

        for j in range(0, n):

            if (nums[j]>second_largest) & (nums[j] != first_largest):
                second_largest = nums[j]
        
        return first_largest, second_largest
    
s = Solution()
print(s.firstAndSecondLargestNumber(nums = [52, -1, 100, 150, 1200, -120.0]))