class Solution(object):
    def firstUniqChar(self, s):
        counts={}
        for i in s:
            if i in counts.keys():
                counts[i]+=1
            else:
                counts[i]=1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        else :
            return -1 




        
        