class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        count_A = 0
        count_B = 0
        for i in range(len(colors)-2):
            if colors[i] == 'A' and colors[i+1] == 'A' and colors[i+2] == 'A':
                count_A += 1
            if colors[i] == 'B' and colors[i+1] == 'B' and colors[i+2] == 'B':
                count_B += 1
        if count_A > count_B:
            return True
        else:
            return False
        