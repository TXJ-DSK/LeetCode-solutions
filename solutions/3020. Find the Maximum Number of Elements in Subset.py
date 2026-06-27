# O(N logMax) Time, O(N) Space, Max is 10^9, can be seen as O(N) Time
from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        result = 0
        for n in cnt.keys():
            if n == 1:
                result = max(result, (cnt[1]+1)//2)
                continue
            num = n
            length = 1
            while cnt[num] > 1 and cnt[num * num] > 0:
                length += 1
                num *= num
            result = max(result, length)
        return result * 2 - 1
