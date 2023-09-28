class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [i for i in nums if i % 2 == 0]+ [j for j in nums if j % 2 != 0]
        return nums
        