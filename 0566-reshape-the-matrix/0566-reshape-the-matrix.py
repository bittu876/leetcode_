class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        ref = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res.append(mat[i][j])
        x = 0
        if len(res) % r == 0:
            for i  in range(r):
                temp = []
                for j in range(len(res)/r):
                    if x<len(res):
                       temp.append(res[x])
                    x = x+1
                ref.append(temp)
            return ref
        else :
            return mat

        