class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        res= [[0 for _ in range(j)] for j in range(1,query_row+2)]
        res[0][0] = poured
        for i in range(query_row):
            for j in range(len(res[i])):
                temp = float(res[i][j]- 1)/2.0
                if temp >0:
                    res[i+1][j] += temp
                    res[i+1][j+1] +=temp
        return res[query_row][query_glass] if res[query_row][query_glass] < 1 else 1
        