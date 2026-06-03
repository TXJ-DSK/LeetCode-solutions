# Recursive backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],5:['j','k','l'], 
        6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

        def recursive(digits: str):
            if len(digits) == 1:
                return mapping[int(digits)]
            letters = mapping[int(digits[0])]
            children = recursive(digits[1:])
            result = [l+c for l in letters for c in children]
            return result
        
        return recursive(digits)
