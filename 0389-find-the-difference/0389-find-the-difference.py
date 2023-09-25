class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        s=list(s)
        t = list(t)
        i = 0
        while i < len(s):
            if s[i]  in t:
                t.remove(s[i])
                s.remove(s[i])   
                i = i -1
            i = i + 1
        res = s + t
        ref= "".join(res)
        return ref
            

        