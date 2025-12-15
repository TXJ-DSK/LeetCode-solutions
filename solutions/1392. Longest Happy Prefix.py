class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ""
        if len(s) == 2:
            if s[0] == s[1]:
                return s[0]
            else:
                return ""
        # Rolling hash parameters
        BASE = 131  # Prime base for polynomial rolling hash
        MOD = 10**9 + 7  # Large prime modulus to prevent overflow
      
        n = len(s)
      
        # Hash values for prefix and suffix
        prefix_hash = 0  # Hash of s[0:i+1]
        suffix_hash = 0  # Hash of reverse of s[0:i+1]

        # Multiplier for suffix hash calculation
        base_power = 1
      
        # Track the longest happy prefix ending position
        longest_happy_prefix = 0

        for i in range(n-1):
            prefix_char = s[i]
            suffix_char = s[n-1-i]
            prefix_val = ord(prefix_char) - ord('a') + 1
            suffix_val = ord(suffix_char) - ord('a') + 1

            # Update prefix hash: hash = hash * base + char_value
            prefix_hash = (prefix_hash * BASE + prefix_val) % MOD
          
            # Update suffix hash: builds hash of reversed string
            # For reversed string, we add new character at the beginning
            suffix_hash = (suffix_hash + suffix_val * base_power) % MOD

            # Update base power for next iteration
            base_power = (base_power * BASE) % MOD

            if prefix_hash == suffix_hash:
                longest_happy_prefix = i + 1
        
        return s[:longest_happy_prefix]

        
