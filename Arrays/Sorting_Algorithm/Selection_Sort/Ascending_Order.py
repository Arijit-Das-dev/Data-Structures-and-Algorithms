"""
Question : Ascending Order using Selection Sort

"""
class Solution(object):

    def ascendingOrder(self, nums):
                
        n = len(nums)

        for i in range(0, n):

            min_num = i

            for j in range(i+1, n):

                if (nums[j] < nums[min_num]):

                    min_num = j

            temp = nums[i]
            nums[i] = nums[min_num]
            nums[min_num] = temp

        return nums
    
s = Solution()
print(s.ascendingOrder(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
))