# O(n^2) time complexity, not worse than (n^2)/4
from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        neg, pos, zero = Counter(), Counter(), 0
        for num in nums:
            if num < 0:
                neg[num] += 1
            elif num > 0:
                pos[num] += 1
            else:
                zero += 1
        if zero > 2:
            result.append([0,0,0])
        if zero > 0:
            for num in pos:
                if neg[-1*num] > 0:
                    result.append([-1*num, 0, num])
        for num in pos:
            for negnum in neg:
                target = 0 - num - negnum
                if target in neg and target > negnum:
                    result.append([negnum, target, num])
                elif target in pos and target < num:
                    result.append([negnum, target, num])
                elif num + negnum * 2 == 0 and neg[negnum] > 1:
                    result.append([negnum, negnum, num])
                elif num * 2 + negnum == 0 and pos[num] > 1:
                    result.append([negnum, num, num])
        return result
