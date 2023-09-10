class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        i=0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(0)
                count = count + 1
                i = i-1
            i = i+1
        for j in range(count):
            nums.append(0)
        return nums

        