class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        c = 0
        for i in range (n):
            for j in range(m):
                if grid[i][j]<0:
                    c+=1
        return c
        