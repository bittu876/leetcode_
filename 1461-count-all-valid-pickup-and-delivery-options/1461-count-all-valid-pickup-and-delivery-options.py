class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod=10**9+7
        ans=math.factorial(n*2)>>n
        return ans%mod