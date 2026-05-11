from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxEle = max(nums)
        maxEleIdx = nums.index(maxEle)
        arr = nums[maxEleIdx:] + nums[:maxEleIdx]
        print(arr)
        result = [-1] * len(arr)
        stack = deque() # Monotonic unique DESC
        stack.append(maxEle)
        for i in range(len(arr)-1, -1, -1):
            num = arr[i]
            while len(stack) > 1 and num >= stack[-1]:
                stack.pop()
            if num == maxEle:
                result[i] = -1
                continue
            result[i] = stack[-1]
            stack.append(num)
        # 1 5 2 3 4 -> 5 2 3 4 1 -> 1 5 2 3 4
        afterMaxEleLen = len(nums) - maxEleIdx
        return result[afterMaxEleLen:] + result[:afterMaxEleLen]
