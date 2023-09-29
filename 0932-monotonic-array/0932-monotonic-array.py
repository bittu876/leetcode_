class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def isMonotone_inc(nums):
            for i in range(len(nums)-1):
                if nums[i] <= nums[i+1]:
                    continue
                else:
                    return False
            else:return True
        def isMonotone_dec(nums):
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    continue
                else:
                    return False
            else:return True
        if isMonotone_inc(nums) or isMonotone_dec(nums):
            return True
        else:return False
        
            
        