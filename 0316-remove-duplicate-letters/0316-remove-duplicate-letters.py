class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        print(last)
        res = str(s[0])
        for i in range(1,len(s)):
            if s[i] not in res:
                if s[i] < res[len(res)-1] and last[res[len(res)-1]] > i:
                        while s[i] < res[len(res)-1] and last[res[len(res)-1]] > i:
                            res = res[:len(res)-1]
                            if len(res) == 0:
                                break
                        res += s[i]
                else:
                    res += s[i] 
        return res

        