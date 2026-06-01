# O(NlogN) time
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        cost_sum = sum(cost)
        cost.sort()
        total_free = 0
        for i in range(len(cost)-3, -1, -3):
            total_free += cost[i]
        return cost_sum - total_free
