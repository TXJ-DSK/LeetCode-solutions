# sliding window, O(N) time, O(1) space
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        elif target < 0:
            return -1
        max_subarr_len = -1
        left, right = 0, 0
        arr_sum = 0
        n = len(nums)
        while right < n:
            arr_sum += nums[right]
            while arr_sum > target:
                arr_sum -= nums[left]
                left += 1
            if arr_sum == target:
                max_subarr_len = max(max_subarr_len, right - left + 1)
            right += 1
        if max_subarr_len == -1:
            return -1
        else:
            return n - max_subarr_len
