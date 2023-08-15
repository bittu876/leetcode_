
def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        m=0
        n=0 
        if divisor<0 :
            m=divisor
            divisor=-divisor
        if dividend<0:
            n=dividend
            dividend=-dividend
        rem=dividend/divisor
        res=int(rem)
        if (m==0 and n==0) or (m>0 and n>0) or (m<0 and n<0):
            res= res
            if res<=(-2)**31:
               res=res+((-2)**31-res)
            elif res>=(2**31)-1:
              res=res-(res-((2**31)-1))
        else:
            res=-res
            if res<=(-2)**31:
               res=res+((-2)**31-res)
            elif res>=(2**31)-1:
              res=res-(res-((2**31)-1))      
        return res


divide(-2147483648,-3)
