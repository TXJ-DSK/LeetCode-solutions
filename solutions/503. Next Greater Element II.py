# monotonic stack, two loops
from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = deque() # monotonic stack DESC storing idx
        for i in range(2*n):
            idx = i % n
            num = nums[idx]
            while len(stack) > 0 and num > nums[stack[-1]]:
                result[stack.pop()] = num
            stack.append(idx)
        return result
