class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.split(" ")
        for i in range(len(res)):
            res[i] = res[i][::-1]
        res=" ".join(res)
        return res

            