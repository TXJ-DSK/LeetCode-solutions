# Time O(NlogN)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key=lambda x: x[0])
        arrows = 1
        x = points[0][0]
        limit = points[0][1]
        for balloon in points[1:]:
            x = balloon[0]
            if x > limit:
                arrows += 1
                limit = balloon[1]
            else:
                limit = min(limit, balloon[1])
        return arrows
