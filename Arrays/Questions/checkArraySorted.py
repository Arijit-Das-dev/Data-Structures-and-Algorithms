"""
Question : Check array sorted or not.

"""

class Solution(object):
    
    def check(self, nums):

        n = len(nums)
        for i in range(0, n-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    

# Example usage:
s = Solution()
print(s.check([1, 2, 3, 4, 5, 6]))
print(s.check([10, 9, 8, 7, 6, 5]))