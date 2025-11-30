from sortedcontainers import SortedList
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1 if nums[0] > 2 * nums[1] else 0
        count = 0
        sl = SortedList([nums[-1]*2])
        for i in range(len(nums)-2, -1, -1):
            count += sl.bisect_left(nums[i])
            sl.add(nums[i]*2)
        return count
