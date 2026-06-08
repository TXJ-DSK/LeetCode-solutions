# O(N) Time, O(1) Space
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ls, eq, ge = [], [], []
        for num in nums:
            if num < pivot:
                ls.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                ge.append(num)
        return ls + eq + ge
