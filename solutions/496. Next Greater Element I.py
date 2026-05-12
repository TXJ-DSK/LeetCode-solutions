# Monotonic stack, O(N + M) time and space
from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {num:-1 for num in nums1}
        stack = deque() # monotonic stack DESC
        for num in nums2:
            while len(stack)>0 and num>stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)
        return [nge[num] for num in nums1]
