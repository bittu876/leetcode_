class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref=""
        for i in s:
            if i.isalpha() or i.isdigit():
                ref = ref + i.lower()
        res=[]
        for i in range(len(ref)-1,-1,-1):
            res.append(ref[i])
        temp = "".join(res)
        if ref == temp:
            return True
        else:
            return False

        