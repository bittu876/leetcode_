#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/
#Find the Index of the First Occurrence in a String



def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype:
    """
    
    if len(needle)>len(haystack):
        return -1
    else:
        for j in range(len(haystack)):
            i=0
            count=0
            if needle[i]==haystack[j]:
                n=0
                for m in range(j,len(haystack)):  
                        if n==len(needle):
                            break
                        else :
                            if needle[n]==haystack[m]:
                                count+=1
                        n=n+1
             
                if count==len(needle):
                    break
        if count==len(needle):
            return j
        else:
            return -1
if __name__=="__main__":
    
    haystack="leetcode"
    needle="code"
    result=strStr(haystack, needle)
    print(f"index of first occurrence of  {needle} in {haystack} is {result}".format(needle,haystack,result))    
