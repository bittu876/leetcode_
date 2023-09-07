class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        ref = [[ 0 for  _ in range (len(text2)+1)] for _ in range(len(text1)+1)]
        print (ref)
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    ref[i][j] = 1 + ref[i+1][j+1]
                else:
                    ref[i][j]=max(ref[i+1][j],ref[i][j+1])

        return ref[0][0]
        