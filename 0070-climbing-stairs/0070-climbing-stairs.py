class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        j=1
        for k in range (n):
            res = i+j
            i = j
            j = res
        return res

        
        