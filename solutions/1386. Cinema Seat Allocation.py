# O(M) time, O(M) space, M is the length of reservedSeats
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # vacant block in left, mid, right, for rows with reserve(smaller than n)
        vacant = dict()
        for row, col in reservedSeats:
            if row not in vacant:
                vacant[row] = [True, True, True]
            if 2 <= col <= 5:
                vacant[row][0] = False
            if 4 <= col <= 7:
                vacant[row][1] = False
            if 6 <= col <= 9:
                vacant[row][2] = False
        result = 0
        for i in vacant:
            if vacant[i][0] and vacant[i][2]:
                result += 2
            elif vacant[i][0] or vacant[i][1] or vacant[i][2]:
                result += 1
        return result + (n - len(vacant)) * 2
