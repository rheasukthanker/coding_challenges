'''Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).'''
# TC: O(n*m) SC: O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if i == 0 and j == 0:
                        cnt += 1
                    elif i == 0 and j > 0:
                        if board[i][j-1] == ".":
                            cnt += 1
                    elif i > 0 and j == 0:
                        if board[i-1][j] == ".":
                            cnt += 1
                    else:
                        if board[i][j-1] == '.' and board[i-1][j] == '.':
                            cnt += 1
        return cnt   
