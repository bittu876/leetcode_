class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = {}
        for i in nums:
            if i in ref:
                ref[i] = ref[i] + 1
            else:
                ref[i] = 1
        mej = 0
        res = 0
        for i in nums:
            if ref[i] > mej:
                mej = ref[i]
                res = i   
        return res
        
        
        