class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                res.append(nums[i])
                nums=nums[:i]+nums[i+1:]
                i -= 1
            i += 1
        return res+nums
        