# O(1) time, O(1) space
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_overlap = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
        y_overlap = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))
        return x_overlap > 0 and y_overlap > 0
