# O(M*N) time, O(M*N) space
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = []
        for row in mat:
            flat.extend(row)
        result = []
        for i in range(r):
            result.append(flat[i*c : (i+1)*c])
        return result
