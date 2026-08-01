# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # Check for the boundaries and if the cell is water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark the cell as visited (sink the island)
            grid[r][c] = '0'  
            # Visit all adjacent land cells (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)  # Start DFS to sink the island

        return num_islands