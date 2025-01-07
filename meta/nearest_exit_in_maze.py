'''You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.'''
# TC: O(m+m) SC: O(m+n)
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cells = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        rows, cols = len(maze), len(maze[0])
        while cells:
            r, c, steps = cells.popleft()
            check = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for i,j in check:
                if i >= 0 and j >= 0 and i < rows and j < cols and maze[i][j] == ".":
                    if i == 0 or j == 0 or i == rows - 1 or j == cols -1:
                        return steps + 1
                    cells.append((i, j, steps + 1))
                    maze[i][j] = "+"
        return -1
