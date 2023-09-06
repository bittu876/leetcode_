class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res=[]
        result =""
        big = str( max(int(a),int(b)))
        small= str (min(int(a),int(b)))
        small = small.zfill(len(str(big)))
        for i in range(len(str(big))-1,-1,-1):
            sum1 =int(big[i]) + int(small[i]) + carry
            res.append(str(sum1 % 2)) 
            carry = sum1//2 
        if carry == 1:
            res.append("1")
        ref=[]
        for j in range(len(res)-1,-1,-1):
            ref.append(res[j])
        result = "".join(ref)
        return result





        