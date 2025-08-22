class Solution:
    from typing import List

    def minimumArea(self, grid: List[List[int]]) -> int:
        top = float('inf')
        bottom = -float('inf')
        left = float('inf')
        right = -float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        if top == float('inf'):  # No 1s found
            return 0
        return (bottom - top + 1) * (right - left + 1)
