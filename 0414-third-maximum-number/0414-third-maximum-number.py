class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in nums:
            if i not in res:
                res.append(i)
        res.sort()
        if len(res)<3:
            return max(res)
        return res[len(res)-3]
               