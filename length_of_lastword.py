#Length of Last Word
#https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord( s):
    """
    :type s: str
    :rtype: int
    """
    s=s.strip()
    count=0
    for i in range(len(s)-1,-1,-1):
        if count!=0 and s[i]==" ":
            break
        else:
            count+=1
    return count
if __name__=="__main__":
    
    s="hello world"
    result=lengthOfLastWord(s)
    print("length of last word is",result)
   
