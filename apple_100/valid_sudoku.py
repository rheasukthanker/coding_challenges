from itertools import chain
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=len(board)
        for i in range(r):
            row=board[i]
            d={}
            for x in row:
                if (x!="."):
                    d[x]=d.get(x,0)+1
                    if d[x]>1:
                        return False
        board_t=list(zip(*board))
        c=len(board_t)
        #print(board)
        #print(board_t)
        for i in range(c):
            col=board_t[i]
            d={}
            for x in col:
                if (x!="."):
                    d[x]=d.get(x,0)+1
                    if d[x]>1:
                        return False
        for i in range(3,r+1,3):
            rows=board[i-3:i]
            rows_t=list(zip(*rows))
            rows1=rows_t[0:3]
            rows1=list(chain.from_iterable(rows1))
            #print(rows)
            d={}
            for x in rows1:
                if (x!="."):
                    d[x]=d.get(x,0)+1
                    if d[x]>1:
                        #print(rows)
                        return False
            rows2=rows_t[3:6]
            rows2=list(chain.from_iterable(rows2))
            #print(rows)
            d={}
            for x in rows2:
                if (x!="."):
                    d[x]=d.get(x,0)+1
                    if d[x]>1:
                        #print(rows)
                        return False  
            rows3=rows_t[6:9]
            rows3=list(chain.from_iterable(rows3))
            #print(rows)
            d={}
            for x in rows3:
                if (x!="."):
                    d[x]=d.get(x,0)+1
                    if d[x]>1:
                        #print(rows)
                        return False
            
        return True