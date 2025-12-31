class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        upper = self.combine(n-1, k)
        upper_left = self.combine(n-1, k-1)
        for c in upper_left:
            c.append(n)
        upper_left.extend(upper)
        return upper_left
