# O(N) time, O(N) space
from collections import Counter
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller, occurence = 0, 0
        for i in range(len(nums)):
            if nums[i] < target:
                smaller += 1
            elif nums[i] == target:
                occurence += 1
        return [i for i in range(smaller, smaller+occurence)]
