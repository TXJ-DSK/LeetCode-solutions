# O(N + KlogK) Time, O(K) space, where K is the number of distinct prices
from collections import Counter
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = Counter(costs)
        result = 0
        for cost in sorted(list(cnt.keys())):
            if cost * cnt[cost] <= coins:
                coins -= cost * cnt[cost]
                result += cnt[cost]
                #print(f"coins={coins},result={result},cost={cost},nums={cnt[cost]}")
                continue
            result += (coins // cost)
            return result
        return result
# Solution 2, trade space for time, O(N + M) Time, O(M) space, where M is the maximum price
from collections import Counter
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = Counter(costs)
        max_cost = max(cnt.keys())
        occurrence = [0] * (max_cost + 1)
        result = 0
        for key in cnt:
            occurrence[key] = cnt[key]
        for cost in range(max_cost+1):
            #print(f"coins={coins},cost={cost},occ={occurrence[cost]}")
            if occurrence[cost] == 0:
                continue
            if cost * occurrence[cost] <= coins:
                coins -= cost * occurrence[cost]
                result += occurrence[cost]
                continue
            return result + coins // cost
        return result
