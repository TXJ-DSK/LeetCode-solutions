# equivalent to flip up to 2 consecutive non-empty 0 blocks to 1, then get the number of 1s
# O(N) time, O(1) space
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count_1s = 0
        max_flips = 0
        prev_0s_block_length = 0
        curr_0s_block_length = 0
        i = 0
        for c in s:
            if c == '0':
                curr_0s_block_length += 1
            if prev_0s_block_length > 0 and curr_0s_block_length > 0:
                max_flips = max(max_flips, prev_0s_block_length + curr_0s_block_length)
            if c == '1':
                count_1s += 1
                if curr_0s_block_length > 0:
                    prev_0s_block_length = curr_0s_block_length
                curr_0s_block_length = 0
        return count_1s + max_flips
