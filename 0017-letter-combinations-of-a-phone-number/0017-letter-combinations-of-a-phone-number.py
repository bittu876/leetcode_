class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keys={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        if len(digits) == 0:
            return []
        def combine(index,res):
            if index == len(digits):
                result.append(''.join(res))
                return
            digit=digits[index]
            num=keys[digit]
            for i in num:
                res.append(i)
                combine(index+1,res)
                res.pop()
        combine(0,[])
        return result