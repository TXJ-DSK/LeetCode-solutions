# O(1) time, O(1) space
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def datePosition(s: str) -> int:
            pos = 0
            month = int(s[:2])
            for i in range(month-1):
                pos += days_per_month[i]
            pos += int(s[3:])
            return pos
        arriveA, leaveA = datePosition(arriveAlice), datePosition(leaveAlice)
        arriveB, leaveB = datePosition(arriveBob), datePosition(leaveBob)
        maxArrive = max(arriveA, arriveB)
        minLeave = min(leaveA, leaveB)
        return max(0, minLeave - maxArrive + 1)
