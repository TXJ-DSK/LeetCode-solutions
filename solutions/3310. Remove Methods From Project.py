# O(V+E) time, O(V+E) space
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        invoke = [set() for _ in range(n)]
        backtrack = [set() for _ in range(n)]
        for i, j in invocations:
            invoke[i].add(j)
            backtrack[j].add(i)
        suspicious = {k}
        #print(f"invoke={invoke}")
        #print(f"backtrack={backtrack}")

        def dfs(method):
            for m in invoke[method]:
                if m not in suspicious:
                    suspicious.add(m)
                    dfs(m)
        dfs(k)
        #print(f"suspicious={suspicious}")


        for m in suspicious:
            for invoker in backtrack[m]:
                if invoker not in suspicious: # cannot remove all
                    return [i for i in range(n)]
        
        result = []
        for i in range(n):
            if i not in suspicious:
                result.append(i)
        return result
