class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # the index of the day that we're gonna buy the stock
        buyPoint = -1
            
        for index,price in enumerate(prices):
            if buyPoint <= -1 or price < prices[buyPoint]:
                buyPoint = index
            else: maxProfit = max(price - prices[buyPoint], maxProfit)
        
        return maxProfit