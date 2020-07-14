class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=0
        profit = 0
        
        length_prices = len(prices)
        
        while buy < length_prices-1:
            
            # Setting buy index
            while prices[buy] > prices[buy+1]:
                buy+=1
                if buy == length_prices-1:
                    break
            
            if buy<length_prices-1:
                sell = buy+1
            else:
                break
                
            # Setting sell index
            if sell < length_prices-1:
                while prices[sell] < prices[sell+1]:
                    sell+=1
                    if sell==length_prices-1:
                        break    
                
            profit += prices[sell]- prices[buy]
            buy= sell+1
            
        return profit