# https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def traverse_island(i,j):
            if grid[i][j]=="1":
                grid[i][j]="0"
                if i!=num_rows-1:
                  traverse_island(i+1,j)
                if j!=num_cols-1:
                  traverse_island(i,j+1)
                if i!=0:
                   traverse_island(i-1,j)
                if j!=0:
                   traverse_island(i,j-1)
            return 
        num_islands = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j]=="1":
                    num_islands = num_islands+1
                    traverse_island(i,j)
        return num_islands
