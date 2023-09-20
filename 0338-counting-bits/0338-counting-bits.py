class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def binary(n):
            binry= ""
            while n>0:
                binry=str(n%2)+binry
                n = n//2
            return binry
        res = []
        for  i in range(n+1):
            binery=binary(i)
            count = 0
            for j in binery:
                if j == "1":
                    count =count+1
            res.append(count)
        return res

        