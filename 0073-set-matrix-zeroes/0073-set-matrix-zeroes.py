class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "0"
                    for l in range(len(matrix)):
                        if matrix[l][j] != 0:
                            matrix[l][j] = "0"
        for i in range(len(matrix)):
            for j in range(len(matrix[i])): 
                if matrix[i][j] == "0":
                     matrix[i][j] = 0
        return matrix