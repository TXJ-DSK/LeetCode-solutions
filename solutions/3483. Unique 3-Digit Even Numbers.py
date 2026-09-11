# O(N) time, O(1) space
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1
        
        result = 0
        for d2 in range(1, 10):
            if cnt[d2] == 0:
                continue
            cnt[d2] -= 1

            for d0 in range(0, 10, 2):
                if cnt[d0] == 0:
                    continue
                cnt[d0] -= 1
                
                for d1 in range(0, 10):
                    if cnt[d1] > 0:
                        result += 1
                
                cnt[d0] += 1
            
            cnt[d2] += 1
        return result
