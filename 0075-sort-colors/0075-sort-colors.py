class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            low = nums[i]
            for j in range(i-1,-1,-1):
                if low < nums[j]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
        return nums
        
        