from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        result = [-1] * n
        numToIdx = dict()
        for i in range(n):
            numToIdx[nums1[i]] = i
        stack = deque()
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            while len(stack) > 0 and num > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                stack.append(num)
                continue
            nge = stack[-1]
            if num in numToIdx:
                result[numToIdx[num]] = nge
            stack.append(num)
        return result
            
