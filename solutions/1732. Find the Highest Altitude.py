# A slightly better solution uses itertools.accumulate
# Time complexity is the same, but more optimized
# But it takes O(N) space, where my solution is O(1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr = 0
        # simply iterate throught the list, get current altitude, and maintain a historic maximum
        for i in gain:
            curr += i
            max_altitude = max(curr, max_altitude)
        return max_altitude
