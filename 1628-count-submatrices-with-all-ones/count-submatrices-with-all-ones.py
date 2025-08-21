class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0

        
        for i in range(m):
            for j in range(n):
                if mat[i][j] and j > 0:
                    mat[i][j] += mat[i][j - 1]

        
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 0:
                    continue
                width = mat[i][j]
                for k in range(i, -1, -1):
                    width = min(width, mat[k][j])
                    res += width

        return res


            