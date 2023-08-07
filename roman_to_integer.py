#Roman to Integer
#https://leetcode.com/problems/roman-to-integer/submissions/
def romanToInt(s):
    """
    :type s: str
    :rtype: bool
    """    
    result=0
    i=0
    s=s.upper()
    while i<len(s):
        if s[i]=="I" :
            if i+1 < len(s):
                if s[i+1]=="V":
                    result=result+4
                    i=i+1                     
                elif s[i+1]=="X":
                    result=result+9
                    i=i+1
                else:
                    result=result+1  
                    
            else:
                result=result+1              
        elif s[i]=="V":
            result=result+5
        elif s[i]=="X":
            if i+1 < len(s):
                if s[i+1]=="L":
                    result=result+40
                    i=i+1
                elif s[i+1]=="C":
                    result=result+90
                    i=i+1
                else:
                    result=result+10
            else:
                result=result+10
        elif s[i]=="L":
            result=result+50
        elif s[i]=="C":
            if i+1 < len(s):
                if s[i+1]=="D":
                    result=result+400
                    i=i+1
                elif s[i+1]=="M":
                    result=result+900
                    i=i+1
                else:
                    result=result+100
            else:        
                result=result+100
        elif s[i]=="D":
            result=result+500
        elif s[i]=="M":
            result=result+1000
        i=i+1          
    return result
if __name__=="__main__":
    s=input("enter roman number")
    result=romanToInt(s)
    print(f"the value of {s} is {result}".format(result))
