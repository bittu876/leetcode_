class Solution(object):
    def multiply(self,num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ex={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        ex1=["0","1","2","3","4","5","6","7","8","9"]
        n=0
        m=0
        for i in range(len(num1)-1,-1,-1):
            j=num1[i]
            n=n+ex[j]*(10**(len(num1)-(i+1)))
        for i in range(len(num2)-1,-1,-1):
            j=num2[i]
            m=m+ex[j]*(10**(len(num2)-(i+1)))
        x=n*m
        res=""
        if x==0:
            res="0"
        else:
            while x!=0:
                num=x%10
                res=ex1[num]+res
                x=x//10
        return res
        
        
        