class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            if i+1==len(nums):
                res=i+1
            if nums[i]==target :
                res=i
                break
            if nums[i]>target:
                res=i
                break
        return res