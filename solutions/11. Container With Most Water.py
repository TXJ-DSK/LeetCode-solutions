# Two pointers, O(N) time, O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # find i, j with maximum (j-i) * min(height[i], height[j])
        i, j = 0, len(height)-1
        max_area = 0
        def calArea(i, j) -> int:
            return (j-i) * min(height[i], height[j])
        while i < j:
            max_area = max(calArea(i, j), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
