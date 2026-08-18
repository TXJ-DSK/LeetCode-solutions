# O(N) time, O(N) space
from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if k == len(nums):
            return max(nums)
        cnt = Counter(nums)
        result = -1
        if k == 1:
            for i in cnt:
                if cnt[i] == 1:
                    result = max(result, i)
            return result
        else:
            head, tail = nums[0], nums[-1]
            if cnt[head] == 1:
                result = max(result, head)
            if cnt[tail] == 1:
                result = max(result, tail)
            return result
