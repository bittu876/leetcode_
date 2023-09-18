import  sys
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        resl=[]
        res=[]
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count =count+1
            res.append(count)
        print(res)
        i = 0
        count = 0
        while count<k:
            resl.append(res.index(min(res)))
            res[res.index(min(res))] =9999999
            count = count+1
        return resl

        