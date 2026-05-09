import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bullsCount = 0
        secretCnt = Counter()
        guessCnt = Counter()
        for i in range(n):
            if secret[i] == guess[i]:
                bullsCount += 1
            else:
                secretCnt[secret[i]] += 1
                guessCnt[guess[i]] += 1
        cows = secretCnt & guessCnt
        cowsCount = cows.total()
        return f"{bullsCount}A{cowsCount}B"
