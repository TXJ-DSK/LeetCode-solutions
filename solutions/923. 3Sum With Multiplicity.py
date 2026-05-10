# O(n^2), use counter to reduce n from length of arr to number of unique integers
from collections import Counter
import math
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 1000000007
        cnt = Counter(arr)
        nums = sorted(list(cnt.keys()))
        result = 0
        for i in range(len(nums)):
            v1 = nums[i]
            for j in range(i, len(nums)):
                v2 = nums[j]
                v3 = target - v1 - v2
                if cnt[v3] == 0:
                    continue
                if v3 < v2:
                    continue
                if v1 == v2 and v2 == v3 and cnt[v1] > 2:
                    result = (result + math.comb(cnt[v1], 3)) % mod
                elif v1 == v2 and v2 != v3 and cnt[v1] > 1:
                    result = (result + math.comb(cnt[v1], 2) * cnt[v3]) % mod
                elif v2 == v3 and v1 != v2 and cnt[v2] > 1:
                    result = (result + math.comb(cnt[v2], 2) * cnt[v1]) % mod
                elif v1 != v2 and v2 != v3:
                    result = (result + cnt[v1] * cnt[v2] * cnt[v3]) % mod
                
        return result % mod
