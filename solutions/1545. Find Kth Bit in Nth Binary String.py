class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        depth = 1
        mid = 0
        while depth < n:
            mid = mid * 2 + 1
            depth += 1
        currk = k-1 # Change to 0-indexed for easier calculation
        flips = 0
        base = -1
        while depth > 0:
            #print(f"mid={mid},currk={currk},depth={depth}")
            if currk == 0:
                base = 0
                break
            if currk == mid:
                base = 1
                break
            if currk > mid:
                flips += 1
                currk = 2 * mid - currk
            mid = (mid - 1) // 2
            depth -= 1
        if base < 0:
            raise Exception("Error, invalid input")
        #print(f"base={base},flips={flips}")
        result = (base + (flips%2)) % 2
        return str(result)
