class Solution:
    def sumScores(self, s: str) -> int:
        return sum(self.calculate_z(s)) + len(s)
    
    def calculate_z(self, s: str):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        
        for i in range(1, n):
            # Case 2: Inside the box
            if i <= r:
                k = i - l
                # Case 2a: Value stays within the box
                if z[k] < r - i + 1:
                    z[i] = z[k]
                # Case 2b: Value touches boundary, need to extend
                else:
                    # Start matching from the known boundary (r)
                    l = i
                    while r < n and s[r] == s[r - l]:
                        r += 1
                    z[i] = r - l
                    r -= 1
            
            # Case 1: Outside the box
            else:
                l, r = i, i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
                
        return z

