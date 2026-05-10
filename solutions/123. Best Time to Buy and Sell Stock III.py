class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        two dps, one swip left to right, one swip right to left
        O(n) time and space
        '''
        dp1 = [0] * len(prices) # profit of first transaction until index, left to right
        minPrice1 = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice1:
                minPrice1 = prices[i]
            else:
                dp1[i] = prices[i] - minPrice1
            dp1[i] = max(dp1[i], dp1[i-1])
        
        dp2 = [0] * len(prices) # profit of second transaction until index, right to left
        maxPrice2 = prices[len(prices)-1] # maximum sell price in second trans
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > maxPrice2:
                maxPrice2 = prices[i]
            else:
                dp2[i] = maxPrice2 - prices[i]
            dp2[i] = max(dp2[i], dp2[i+1])
        result = 0
        for i in range(len(prices)):
            result = max(result, dp1[i] + dp2[i])
        return result
