# O(Nr) time, O(N) space
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        result = -1
        for arrLen in range(l, r+1):
            for i in range(len(prefixSum) - arrLen):
                arrSum = prefixSum[i + arrLen] - prefixSum[i]
                if result < 0 and arrSum > 0:
                    result = arrSum
                if arrSum > 0 and arrSum < result:
                    result = arrSum
        return result
