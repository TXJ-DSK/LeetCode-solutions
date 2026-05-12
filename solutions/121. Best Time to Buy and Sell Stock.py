# 1 traversal, O(N) time, O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for price in prices:
            if price < minBuy:
                minBuy = price
            else:
                profit = max(profit, price - minBuy)
        return profit
