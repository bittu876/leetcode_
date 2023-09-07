class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        x=[[ 1 for _ in range(i) ] for i in range(1,rowIndex+2) ]
        print(x)
        for i in  range(len(x)):
            for j in range(len(x[i])):
                if j != 0 and j != len(x[i])-1:
                    x[i][j]=x[i-1][j-1]+x[i-1][j]
        return x[len(x)-1]
        