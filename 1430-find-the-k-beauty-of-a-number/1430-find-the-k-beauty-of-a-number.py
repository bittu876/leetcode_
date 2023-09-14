class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        string = str(num)
        count = 0
        for i in range(len(string)-k+1):
            ref = string[i:i+k]
            if int(ref) != 0:
                if num % int(ref) == 0:
                    count =count+1 
        
        return count
        