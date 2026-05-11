class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        i, j = 0, 0
        count = 0
        maxCount = 0
        result = 1
        while i < len(start):
            # when one meeting start before one ends, need one additional meeting room
            if start[i] < end[j]:
                count += 1
                maxCount = max(maxCount, count)
                i += 1
            # when one meeting ends at or before one starts, clear one meeting room
            else:
                count -= 1
                j += 1
        return maxCount
        
