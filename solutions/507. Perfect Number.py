# O(N^1/2) time, O(1) space
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divisors_sum = 1
        for i in range(2, math.floor(math.sqrt(num))+1):
            if num % i == 0:
                divisors_sum += i
                if num // i != i:
                    divisors_sum += num // i
                if divisors_sum > num:
                    return False
        return divisors_sum == num
