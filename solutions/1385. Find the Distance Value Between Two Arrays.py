# O(NlogN) time, O(1) extra space
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        satisfied = 0
        n = len(arr2)-1
        for num in arr1:
            left, right = 0, n
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] - d <= num <= arr2[mid] + d:
                    satisfied += 1
                    break
                if arr2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return len(arr1) - satisfied
