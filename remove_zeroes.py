class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos_A = 0
        for index in range (len(nums)-1):
            if nums[index] != 0:
                pos_A += 1
            else:
                if nums[index+1] != 0:
                    temp = nums[pos_A]
                    nums[pos_A] = nums[index+1]
                    nums[index+1] = temp
                    pos_A += 1
                
    def printList(self,nums):
        for value in nums:
            print value

solution = Solution()
nums = [1,2,0,0,0,2,3,4,5,0,0,9,9]
solution.moveZeroes(nums)
solution.printList(nums)