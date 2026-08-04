# O(N) time, O(N) space
from collections import Counter
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        min_num, max_num = min(nums), max(nums)
        result = []
        for i in range(min_num, max_num):
            if i not in cnt:
                result.append(i)
        return result
