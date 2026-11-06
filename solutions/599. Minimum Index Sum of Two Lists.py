# O(N) time, O(N) space
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        common = set(list1) & set(list2)
        eleIdx1, eleIdx2 = dict(), dict()
        for idx, ele in enumerate(list1):
            eleIdx1[ele] = idx
        for idx, ele in enumerate(list2):
            eleIdx2[ele] = idx
        #print(eleIdx1)
        #print(eleIdx2)
        result = []
        leastIdxSum = 9999
        for ele in common:
            idxSum = eleIdx1[ele] + eleIdx2[ele]
            if idxSum < leastIdxSum:
                result = [ele]
                leastIdxSum = idxSum
            elif idxSum == leastIdxSum:
                result.append(ele)
        return result
