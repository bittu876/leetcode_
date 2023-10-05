class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindram(substring):
            return substring == substring[::-1]
        n= len(s)
        for i in range(n,0,-1):
            for j in range(n-i+1):
                if isPalindram(s[j:j+i]):
                    return s[j:j+i]  
        
