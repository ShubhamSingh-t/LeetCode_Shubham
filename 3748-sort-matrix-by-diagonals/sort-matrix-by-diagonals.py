from collections import defaultdict

class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        diagonals = defaultdict(list)

        # Step 1: Collect elements by diagonal index
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        # Step 2: Sort each diagonal
        for key in diagonals:
            if key >= 0:
                diagonals[key].sort(reverse=True)  # Bottom-left: non-increasing
            else:
                diagonals[key].sort()              # Top-right: non-decreasing

        # Step 3: Reassign sorted values back to grid
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)

        return grid
            