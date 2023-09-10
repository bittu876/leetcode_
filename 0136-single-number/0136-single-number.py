class Solution(object):
    def singleNumber(self, nums):
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
        for i in nums:
            if ref[i] == 1:
                return i 
        