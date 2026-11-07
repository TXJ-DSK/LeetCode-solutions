# O(N) time, O(1) extra space
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        available = 0
        if len(flowerbed) == 1:
            return 1-flowerbed[0] >= n
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            available += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            available += 1
            flowerbed[-1] = 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                available += 1
                flowerbed[i] = 1
        return available >= n
