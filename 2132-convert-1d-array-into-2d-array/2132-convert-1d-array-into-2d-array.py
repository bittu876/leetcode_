class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) % m != 0:
            return []
        if len(original) / m != n:
            return []
        x = 0
        res = []
        for i in range(m):
            temp=[]
            for j in range(n):
                if x<len(original):
                    temp.append(original[x])
                x= x+1
            res.append(temp)
        return res

        