# storing all positions of 1s, O(N^2) time,O(N) space
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one_idx = []
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                one_idx.append(i)
        m = len(one_idx)
        if m < k:
            return ""
        #print(one_idx)
        result = one_idx
        for i in range(m-k+1):
            aligned = [idx-one_idx[i] for idx in one_idx[i:i+k]] # 0-aligned indexes of 1
            #print(i, aligned)
            if one_idx[i+k-1] - one_idx[i] < result[-1] - result[0]: #shorter
                result = aligned
            elif one_idx[i+k-1] - one_idx[i] > result[-1] - result[0]: #longer
                continue
            elif aligned > result:
                result = aligned
        b_list = ["1"]
        for i in range(1, len(result)):
            if result[i] - result[i-1] > 1:
                b_list.append("0" * (result[i] - result[i-1] - 1))
            b_list.append("1")
        return "".join(b_list)
