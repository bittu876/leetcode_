class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s.split(" ")
        res = res[::-1]
        i = 0
        while i < len(res):
            if res[i] == '':
                res = res[:i]+res[i+1:]
                i -= 1
            i += 1
        ref = " ".join(res)
        return ref
        