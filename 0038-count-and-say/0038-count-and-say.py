class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int                 #1211
        :rtype: str
        """
        if n==1:
            return "1"
        if n == 2:
            return "11"
        result = ""
        basic  = "11"
        for i in range(3,n+1):
            res = []
            count = 0
            temp=""
            for j in range (len(basic)):
                if len(res) == 0:
                    res.append(basic[j])
                    count = 1
                else:
                    if basic[j] == res[0]:
                        count = count + 1
                    else:
                        temp = temp + str(count) + basic[j-1]
                        res = []
                        res.append(basic[j])
                        count = 1
                    if j == len(basic) -1 :
                        temp = temp + str(count) + res[0]
            basic =temp
        result=basic
        return result
        