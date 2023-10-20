class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ref = [[0 for _ in range(len(board[i]))] for i in range(len(board))]
        n = len(board)
        for i in range (n):
            for j in range(len(board[i])):
                ref[i][j] = board[i][j]
        for i in range (n):
            for j in range(len(board[i])):
                count_0 = 0
                count_1 = 0
                for k in [[0,1],[0,-1],[1,0],[1,-1],[1,1],[-1,0],[-1,-1],[-1,1]]:
                    if i+k[0] >=0 and i+k[0] < n and j+k[1] >=0 and j+k[1] < len(board[i]):
                        if ref[i+k[0]][j+k[1]] == 0:
                            count_0 += 1
                        else:
                            count_1 += 1
                if ref[i][j] == 1:
                    if count_1 < 2 or count_1 >3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                else:
                    if count_1 == 3:
                        board[i][j] = 1
            

