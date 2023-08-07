#Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/submissions/
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack=[]
    result=False
    for i in range(len(s)):
        if s[i]=="[" or s[i]=="{" or s[i]=="(" :
            stack.append(s[i])
        elif s[i]=="}":
            if len(stack)==0 or stack[len(stack)-1]!="{" :
                stack.append(s[i])
            else:
                
                    stack.pop()
        elif s[i]=="]":
            if len(stack)==0 or stack[len(stack)-1]!="[" :
                stack.append(s[i])
            else:
                
                    stack.pop()
        elif s[i]==")":
            if len(stack)==0 or stack[len(stack)-1]!="(" :
                stack.append(s[i])
            else:
                
                    stack.pop()
    if len(stack)==0:
        result=True      
    return result
if __name__=="__main__":
    s=input("enter a string of parentheses")
    
    result=isValid(s)
    if result:
        print("valid parentheses")
    else:
        print("not a valid parentheses")

