def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        con={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        x=con.keys()
        list(x)
        print(x)
        res=0
        count=0
        roman=""
        m=0
        while num>0:
            res=(num%10)*(10**count)
            count+=1
            print(res)
            sub_string=""
            while res>0: 
                for i in x:
                    if res >=i:
                        m=i
                sub_string=sub_string+con[m]
                res=res-m
            roman=sub_string+roman
            
            num=num//10
            
        return roman
x=intToRoman(1994)
print(x)
