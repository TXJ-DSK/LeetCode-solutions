# O(N) time, O(N) space
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        n = len(nums)
        result = 0
        head, tail = 0, 0
        while tail < n:
            cnt[nums[tail]] += 1
            while cnt[nums[tail]] > k:
                cnt[nums[head]] -= 1
                head += 1
            tail += 1
            result = max(result, tail - head)
        return result
