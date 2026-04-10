class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,-9,-5,-4,-3,-9]
        # [10,1,4,5,6,0]
        buy = 0
        sell = 1
        max_p = 0

        while(sell < len(prices)):
            if prices[buy] < prices[sell]:
                max_p = max(max_p, prices[sell] - prices[buy])
            else:
                buy = sell
            sell+=1

        return max_p



