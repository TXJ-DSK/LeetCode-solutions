# O(N + M) Time, O(1) Space, N is length of landStartTime, M is length of waterStartTime
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_end = landStartTime[0] + landDuration[0]
        for i in range(len(landStartTime)):
            min_land_end = min(min_land_end, landStartTime[i] + landDuration[i])
        min_water_end = waterStartTime[0] + waterDuration[0]
        for i in range(len(waterStartTime)):
            min_water_end = min(min_water_end, waterStartTime[i] + waterDuration[i])
        
        # a guaranteed finish time
        result = landStartTime[0] + landDuration[0] + waterStartTime[0] + waterDuration[0]
        # first land then water
        for i in range(len(waterStartTime)):
            result = min(result, max(min_land_end, waterStartTime[i]) + waterDuration[i])
        # first water then land
        for i in range(len(landStartTime)):
            result = min(result, max(min_water_end, landStartTime[i]) + landDuration[i])
        return result
