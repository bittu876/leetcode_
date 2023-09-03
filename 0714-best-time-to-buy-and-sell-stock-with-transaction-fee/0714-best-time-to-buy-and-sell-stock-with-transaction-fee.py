class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = -prices[0]
        profit =0
        for i in range(1,len(prices)):
            buy=max(buy,profit - prices[i])
            profit=max(profit, prices[i]+buy -fee)
        return profit



        