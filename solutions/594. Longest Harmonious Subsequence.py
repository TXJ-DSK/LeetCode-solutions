# O(N) time, O(N) space
from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        result = 0
        cnt = Counter(nums)
        for n in cnt:
            if n+1 in cnt:
                result = max(result, cnt[n]+cnt[n+1])
        return result
