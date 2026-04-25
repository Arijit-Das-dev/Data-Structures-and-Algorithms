"""
Question : Store only unique elemensts

"""

# Approach 1
class Solution1(object):

    def storeUniqueElements(self, nums):

        nextNum = []
        n = len(nums)

        for i in range(0, n):

            if nums[i] not in nextNum:

                nextNum += [nums[i]]

        return nextNum
    
s = Solution1()
print(s.storeUniqueElements([1, 1, 2, 2, 3, 3, 4, 4]))


# Approach 2
class Solution2(object):

    def storeUniqueElements(self, nums):

        nextNum = []

        for elements in nums:
            if elements not in nextNum:

                nextNum += [elements]

        return nextNum
    

s = Solution2()
print(s.storeUniqueElements([1, 1, 2, 2, 3, 3, 4, 4]))