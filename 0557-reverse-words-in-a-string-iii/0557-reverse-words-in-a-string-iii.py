class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        ref = ""
        for i in s:
            if i == " ":
                ref = ref+str(res)[::-1]+i 
                res=""
            else:
                res = res+i
        ref = ref + res[::-1]
        return ref