# https://leetcode.com/problems/swim-in-rising-water/description/

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        visited = set()
        visited.add((0, 0))

        while min_heap:
            elevation, x, y = heapq.heappop(min_heap)
            
            # If we reached the bottom-right corner, return the elevation (time)
            if x == n - 1 and y == n - 1:
                return elevation
            
            # Check all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    # Push the maximum elevation along the path so far to the heap
                    heapq.heappush(min_heap, (max(elevation, grid[nx][ny]), nx, ny))

# Example usage:
solution = Solution()
grid1 = [[0, 2], [1, 3]]
print(solution.swimInWater(grid1))  # Output: 3

grid2 = [[0, 1, 2, 3, 4], 
          [24, 25, 26, 27, 5], 
          [23, 21, 20, 19, 6], 
          [22, 17, 16, 18, 7], 
          [21, 20, 19, 20, 8]]
print(solution.swimInWater(grid2))  # Output: 8