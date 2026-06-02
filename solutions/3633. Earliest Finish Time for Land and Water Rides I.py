# O(N) Time, O(1) Space
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_end = 9999
        min_water_end = 9999
        for i in range(len(landStartTime)):
            if landStartTime[i] + landDuration[i] < min_land_end:
                min_land_end = landStartTime[i] + landDuration[i]
        for i in range(len(waterStartTime)):
            if waterStartTime[i] + waterDuration[i] < min_water_end:
                min_water_end = waterStartTime[i] + waterDuration[i]
        #print(f"min_land_end={min_land_end},min_water_end={min_water_end}")
        # first land then water
        min_water_finish = 9999
        for i in range(len(waterStartTime)):
            if waterStartTime[i] <= min_land_end:
                min_water_finish = min(min_water_finish, min_land_end + waterDuration[i])
            else:
                min_water_finish = min(min_water_finish, waterStartTime[i] + waterDuration[i])
        # first water then land
        min_land_finish = 9999
        for i in range(len(landStartTime)):
            if landStartTime[i] <= min_water_end:
                min_land_finish = min(min_land_finish, min_water_end + landDuration[i])
            else:
                min_land_finish = min(min_land_finish, landStartTime[i] + landDuration[i])

        return min(min_water_finish, min_land_finish)
