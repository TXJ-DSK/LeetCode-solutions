# DFS, O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency = {course: [] for course in range(numCourses)}
        for course, pre in prerequisites:
            dependency[course].append(pre)
        path = set()
        visited = set()
        result = []

        def dfs(course) -> bool:
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for pre in dependency[course]:
                if pre in path:
                    return False
                if pre in visited:
                    continue
                if not dfs(pre):
                    return False
                
            visited.add(course)
            path.remove(course)
            result.append(course)
            return True
        isCycle = False
        for i in range(numCourses):
            if i not in visited:
                isCycle = dfs(i)
                if not isCycle:
                    return []
        return result
