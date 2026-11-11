# O(1) time, O(1) space
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth >= cost1 + cost2:
            return cost1 * need1 + cost2 * need2
        else:
            minBoth = min(need1, need2)
            return costBoth * minBoth + min(costBoth, cost1) * (need1 - minBoth) + min(costBoth, cost2) * (need2 - minBoth)
