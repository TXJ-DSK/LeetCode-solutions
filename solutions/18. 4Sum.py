# O(N^2) Time, O(N^2) Space
from collections import Counter
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        cnt = Counter(nums)
        for n in cnt:
            if cnt[n] > 4:
                cnt[n] = 4
        nums = list(cnt.elements())
        n = len(nums)
        sum2 = dict()
        for i in range(n):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                sum2[s] = sum2.get(s, [])
                sum2[s].append((i, j))
        result = set()
        for k in sum2:
            pair1s = sum2[k]
            if target - k not in sum2:
                continue
            pair2s = sum2[target - k]
            for a, b in pair1s:
                for c, d in pair2s:
                    if a != c and a != d and b != c and b != d:
                        result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
        return [list(idxs) for idxs in result]
