# Simple math, optimized with dp
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        sequential = [i for i in range(1, 10)]
        while len(sequential) > 0:
            sequential.pop(-1)
            new_sequential = []
            for i in sequential:
                d = i % 10
                num = i * 10 + d + 1
                new_sequential.append(num)
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    return result
            sequential = new_sequential
        return result
