class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [-1] * len(score)
        scoreToIdx = dict()
        for i in range(len(score)):
            scoreToIdx[score[i]] = i
        score.sort(reverse=True)
        result[scoreToIdx[score[0]]] = "Gold Medal"
        if n > 1:
            result[scoreToIdx[score[1]]] = "Silver Medal"
        if n > 2:
            result[scoreToIdx[score[2]]] = "Bronze Medal"
        if n > 3:
            for i in range(3,n):
                result[scoreToIdx[score[i]]] = str(i+1)
        return result
