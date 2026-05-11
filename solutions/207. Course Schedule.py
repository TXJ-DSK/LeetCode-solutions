import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        dependency = defaultdict(set)
        for prerequisite in prerequisites:
            dependency[prerequisite[0]].add(prerequisite[1])
        
        def dfs(course) -> bool:
            if course in path:
                return False
            path.add(course)
            visited.add(course)
            for prerequisite in dependency[course]:
                if prerequisite in path:
                    return False
                if prerequisite in visited:
                    continue
                if not dfs(prerequisite):
                    return False
            path.remove(course)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
