# O(E) Time, O(E) Space
# Start with city 1, explore all connected roads and cities
from collections import defaultdict, deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        city_roads = defaultdict(list)
        for r in roads:
            city_roads[r[0]].append(r)
            city_roads[r[1]].append(r)
        dq = deque([r for r in city_roads[1]])
        min_path = 99999999
        visited_city = {1}
        visited_road = set()
        while dq:
            r = dq.popleft()
            min_path = min(min_path, r[2])
            visited_road.add(tuple(r))
            new_city = None
            if r[0] not in visited_city:
                new_city = r[0]
            elif r[1] not in visited_city:
                new_city = r[1]
            else:
                continue
            visited_city.add(new_city)
            for new_road in city_roads[new_city]:
                if tuple(new_road) not in visited_road:
                    dq.append(new_road)
        return min_path
