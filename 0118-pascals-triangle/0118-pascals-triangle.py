class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # creating a structur for out put filling with 1
        #  if numRows = 4  print(x)  ==> 
        #            1
        #           1  1
        #          1  1  1   
        #         1  1  1  1
        x= [[1 for i in range(x)] for x in range(1,numRows+1)]
        for i in  range(len(x)):
            for j in range(len(x[i])):
                if j != 0 and j != len(x[i])-1:
                    x[i][j]=x[i-1][j-1]+x[i-1][j]
        # this nested forloop will change the values in it
        #if the pointr is at starting or ending of the row it doesn't change anything
        #if it is middle of the row it change value by adding previos row precedig col value and current col value
        return x

        
