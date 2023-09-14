class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res1=""
        res2=""
        i = 0
        while i < len(s):
            if s[i] not in res1:
                res1 = res1 + s[i]
            else:
                i = s.index(s[i]) +1
                s= s[i:]
                i = 0
                if len(res1) >=len(res2):
                    res2= res1
                    res1 = ""
                    res1 = res1+s[i]
                else :
                    res1 = ""
                    res1 = res1+s[i]
            i = i + 1
        
        if len(res1) > len(res2) :
            return len(res1)
        else:
            return len(res2)