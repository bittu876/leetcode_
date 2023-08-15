def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=0
        for i in digits:
            res=res*10+i
        res+=1
        res=str(res)
        x=[]
        for i in range(len(res)):
            y=int(res[i])
            x.append(y)
        return x
dig=[5,8,3]
m=plusOne(dig)
print(m)
