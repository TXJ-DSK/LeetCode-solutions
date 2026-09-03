# binary search, O(logN) time, O(1) space
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square < num:
                low = mid + 1
            elif square == num:
                return True
            else:
                high = mid - 1
        return False
