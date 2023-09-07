class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        x= [[1 for i in range(x)] for x in range(1,numRows+1)]
        for i in  range(len(x)):
            for j in range(len(x[i])):
                if j != 0 and j != len(x[i])-1:
                    x[i][j]=x[i-1][j-1]+x[i-1][j]
        return x

        