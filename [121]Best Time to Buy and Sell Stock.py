class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, buy = 0, float('inf')
        for p in prices:
            buy = min(buy, p)
            sell = max(sell, p - buy)
        return sell
