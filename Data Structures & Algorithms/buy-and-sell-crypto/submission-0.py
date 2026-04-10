class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,-9,-5,-4,-3,-9]
        # [10,1,4,5,6,0]
        max_p = 0
        for i in range(len(prices)-1):
            p =  max(prices[i+1:])-prices[i]
            max_p = max(max_p,p)
        return max_p

