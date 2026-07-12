# O(NlogN) Time, O(N) Space
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniques = sorted(list(set(arr)))
        num_rank = dict()
        for i in range(len(uniques)):
            num_rank[uniques[i]] = i+1
        return [num_rank[num] for num in arr]
