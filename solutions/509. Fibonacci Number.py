# O(N) time, O(N) space
class Solution:
    def fib(self, n: int) -> int:
        sequence = [0, 1]
        if n <= 1:
            return sequence[n]
        while len(sequence) - 1 < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[-1]
