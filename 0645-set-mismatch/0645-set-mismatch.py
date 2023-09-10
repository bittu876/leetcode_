class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1,len(nums)+1):
            if nums.count(i) == 2:
                res.append(i)
                for j in range(1,max(nums)+2):
                    if j not in nums:
                        res.append(j)
                        break
                break
        return res
            
        