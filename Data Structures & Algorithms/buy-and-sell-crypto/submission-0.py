class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1: return 0
        
        lowest = float('inf')
        res = 0

        for i, price in enumerate(prices):
            lowest = min(lowest, price)
            res = max(res, price - lowest)

        return res