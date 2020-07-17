class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        for i in range(len(prices)-1):
            profit = 0
            for j in range(i+1,len(prices)):
                if prices[j]> prices[i]:
                    profit = prices[j]-prices[i]
                    if profit > max_profit:
                        max_profit = profit
                        
        return max_profit
    