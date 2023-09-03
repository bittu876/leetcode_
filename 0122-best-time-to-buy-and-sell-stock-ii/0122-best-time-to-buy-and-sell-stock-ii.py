class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -prices[0]
        profit =0
        for i in range(1,len(prices)):
            buy=max(buy,profit - prices[i])
            profit=max(profit, prices[i]+buy)
        return profit

        