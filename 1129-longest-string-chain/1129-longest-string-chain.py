class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words1=sorted(words,key=len)
        res={}
        ref = 0
        for i in words1:
            res[i]=1
            for j in range(len(i)):
                temp = i[:j]+i[j+1:]
                if temp in res:
                    res[i] =max(res[i],res[temp]+1)
                j = j+1
            ref=max(ref,res[i])

        return ref 
