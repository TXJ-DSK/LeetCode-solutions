class Solution:
    def sumScores(self, s: str) -> int:
        total_score = 0
        # Rolling hash parameters
        BASE = 131  # Prime base for polynomial rolling hash
        MOD = 10**9 + 7  # Large prime modulus to prevent overflow

        n = len(s)
      
        # Hash values for prefix
        prefix_hash = 0  # Hash of s[0:i+1]
      
        prefix_hash_values = []

        for i, char in enumerate(s):
            # Calculate character value (1-indexed)
            char_value = ord(char) - ord('a') + 1
          
            # Update prefix hash: hash = hash * base + char_value
            prefix_hash = (prefix_hash * BASE + char_value) % MOD
            prefix_hash_values.append(prefix_hash)
        
        for i in range(n):
            prefix_hash = 0
            score = 0
            for j in range(i, n):
                char_value = ord(s[j]) - ord('a') + 1
                prefix_hash = (prefix_hash * BASE + char_value) % MOD
                if prefix_hash == prefix_hash_values[j-i]:
                    score = j - i + 1
                else:
                    break
            total_score += score
        return total_score
