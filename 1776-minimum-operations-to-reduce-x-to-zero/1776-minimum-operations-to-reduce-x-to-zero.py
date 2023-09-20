class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return n
        left  = 0 
        right = 0
        sum1 = -1
        for i in range(n):
            if right < target:
                right = right + nums[i]
            while right >= target:
                if right == target:
                    sum1=max(sum1,i-left+1)
                right = right - nums[left]
                left = left + 1
        return n - sum1 if sum1!= -1 else -1












        