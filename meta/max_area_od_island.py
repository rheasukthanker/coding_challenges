'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.'''
# TC: O(n*m), SC: O(n*m)
class Solution:
    def dfs(self,grid,r,c):
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
            return 0
        if grid[r][c]==0:
            return 0
        grid[r][c]=0
        return 1 + self.dfs(grid, r - 1, c) + self.dfs(grid, r, c - 1) \
            + self.dfs(grid, r + 1, c) + self.dfs(grid, r, c + 1) 
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0:
                    max_islands = max(max_islands, self.dfs(grid,r,c))
        return max_islands
