class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ref = triangle[len(triangle)-1]
        ref1=[]
        for  i in range(len(triangle)-2 ,-1,-1):
            ref1 = []
            for j in range(len(triangle[i])):
                ref1.append(min(triangle[i][j]+ref[j],triangle[i][j]+ref[j+1]))
            ref =ref1

        return ref[0]

        