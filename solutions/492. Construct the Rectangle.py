# O(N^1/2) time, O(1) space
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        W = math.floor(math.sqrt(area))
        while area % W != 0:
            W -= 1
        return [area // W, W]
