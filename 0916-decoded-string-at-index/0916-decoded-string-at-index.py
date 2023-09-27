class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=0
        i=0
        while res < k:
            if s[i].isdigit():
                res *= int(s[i])
            elif s[i].isalpha():
                res += 1
            i = i+1 
        for j in range(i-1, -1, -1):
            if s[j].isdigit():
                res //= int(s[j])
                k %= res
            else:
                if k == 0 or k == res:
                    return s[j]
                res -= 1
    
        