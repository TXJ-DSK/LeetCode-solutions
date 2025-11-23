class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 3
            else:
                return 2
        
        count = 0
        n = len(s)
        # (start, end) index for a palindromic substring
        p_odd = [(i,i) for i in range(n)]
        # Store all the palindromic substring that have odd length, starting with single character
        # In each iteration, check if charater on left and right of the palindromic substring is the same
        # If so, store it for the next itration
        while p_odd:
            count += len(p_odd)
            new_list = []
            for pair in p_odd:
                if pair[0] - 1 < 0 or pair[1] >= n-1:
                    continue
                if s[pair[0] - 1] == s[pair[1] + 1]:
                    new_list.append((pair[0] - 1, pair[1] + 1))
            p_odd.clear()
            p_odd.extend(new_list)
        # Same method for even length
        p_even = []
        for i in range(n-1):
            if s[i] == s[i+1]:
                p_even.append((i, i+1))
        while p_even:
            count += len(p_even)
            new_list = []
            for pair in p_even:
                if pair[0] - 1 < 0 or pair[1] >= n-1:
                    continue
                if s[pair[0] - 1] == s[pair[1] + 1]:
                    new_list.append((pair[0] - 1, pair[1] + 1))
            p_even.clear()
            p_even.extend(new_list)
        
        return count
