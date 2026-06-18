# Simple math, O(1) space & time
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_deg = 6 * minutes
        hour = hour % 12
        hr_deg = 30 * hour
        hr_deg += min_deg/12
        angle = abs(min_deg - hr_deg)
        angle = min(angle, 360-angle)
        return angle
