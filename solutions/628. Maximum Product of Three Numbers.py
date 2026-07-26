# O(N) time, O(1) space
# 3 most positive multiply, or 2 most negative multiply 1 most positive
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # check if all the numbers are negative or zero
        exist0, existpos = False, False
        for n in nums:
            if n == 0:
                exist0 = True
            elif n > 0:
                existpos = True
        if not existpos:
            if exist0:
                return 0
            larestneg1, larestneg2, larestneg3 = -1000, -1000, -1000
            for n in nums:
                if n > larestneg3:
                    larestneg3 = n
                    larestneg2, larestneg3 = max(larestneg2, larestneg3), min(larestneg2, larestneg3)
                    larestneg1, larestneg2 = max(larestneg1, larestneg2), min(larestneg1, larestneg2)
            return larestneg1 * larestneg2 * larestneg3
            
        # normal logic
        pos1, pos2, pos3, neg1, neg2 = 0, 0, 0, 0, 0
        for n in nums:
            if n > 0:
                if n > pos3:
                    pos3 = n
                    pos2, pos3 = max(pos2, pos3), min(pos2, pos3)
                    pos1, pos2 = max(pos1, pos2), min(pos1, pos2)
            elif n < 0:
                if n < neg2:
                    neg2 = n
                    neg1, neg2 = min(neg1, neg2), max(neg1, neg2)
        return max(pos1 * pos2 * pos3, pos1 * neg1 * neg2)
