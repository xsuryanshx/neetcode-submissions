class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profits = 0
        for i in range(1,len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            elif prices[i] >= min_buy:
                profits = max(prices[i]-min_buy, profits)
            
        return profits



            




