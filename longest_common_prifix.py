#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/description/


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result=""
    lenth=len(strs[0])
    for i in range(len(strs)):
        if lenth>len(strs[i]):
            lenth=len(strs[i])
    for i in range(lenth):
        count=0
        for j in range(len(strs)):
            if j+1<len(strs):
                if strs[j][i]==strs[j+1][i] :
                    count=count+1
        if count==len(strs)-1:
            result=result+strs[j][i]
        else:
            return result
    return result
if __name__=="__main__":
    
    strs=["flower","flight","flow"]
    result=longestCommonPrefix(strs)
    print(f"the longest common prifix amonge {strs} is {result}".format(strs,result))
   
