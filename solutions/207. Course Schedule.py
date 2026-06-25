# O(V + E) Time, O(V) Space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = dict()
        for course, pre in prerequisites:
            if course not in dependency:
                dependency[course] = [pre]
            else:
                dependency[course].append(pre)
        visited = set()
        
        def validate(path, last):
            if last in visited:
                return True
            if last not in dependency:
                visited.add(last)
                return True
            for pre in dependency[last]:
                if pre in path:
                    return False
                path.add(pre)
                if not validate(path, pre):
                    return False
                path.remove(pre)
            visited.add(last)
            return True
        
        for course in range(numCourses):
            if not validate({course}, course):
                return False
        return True
