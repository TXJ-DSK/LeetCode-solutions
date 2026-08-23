# O(N) time, O(1) space
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_sum, right_sum = 0, 0
        left_q, right_q = 0, 0
        for i in range(n):
            if num[i] == '?':
                if i < n//2:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < n//2:
                    left_sum += int(num[i])
                else:
                    right_sum += int(num[i])
        if (left_q + right_q) % 2 == 1:
            return True
        q_diff = left_q - right_q
        if q_diff > 0:
            left_sum += q_diff // 2 * 9
        elif q_diff < 0:
            right_sum += -1 * q_diff // 2 * 9
        #print(f"left_sum={left_sum},right_sum={right_sum}")
        return left_sum != right_sum
