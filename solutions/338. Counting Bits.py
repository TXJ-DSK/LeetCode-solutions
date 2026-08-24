# size of list doubled in each iteration
# O(N) time, O(N) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        while len(result) < n+1:
            result.extend([i+1 for i in result])
        return result[:n+1]
