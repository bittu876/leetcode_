class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sum1 = 0
        for i in nums:
            sum1 = sum1+i
            res.append(sum1)
        return res