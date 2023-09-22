class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        ref = 0
        i = 0
        while i <len(nums):
            sum1 = sum1+nums[i]
            ref = min(ref,sum1)
            i=i+1
        return (-ref)+1
        