class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        def isSafe(row,col):
            arr = board.copy()
            j1 = col
            #Left
            while j1>=0:
                if arr[row][j1]:
                    return False
                j1-=1
            #Left Up Diag
            i,j = row,col
            while i>=0 and j>=0:
                if arr[i][j]:
                    return False
                i-=1
                j-=1
            #Left down diagonal
            i,j = row,col
            while i<n and j>=0:
                if arr[i][j]:
                    return False
                i+=1
                j-=1
            return True
                
        def backtrack(col):
            if col == n:
                arr = board.copy()
                temp = []
                for i in range(n):
                    rowS = ""
                    for j in range(n):
                        if arr[i][j]:
                            rowS+="Q"
                        else:
                            rowS+="."
                    temp.append(rowS)
                ans.append(temp)
                return
            for i in range(n):
                if isSafe(i,col):
                    board[i][col] = 1
                    backtrack(col+1)
                    board[i][col] = 0
        backtrack(0)
        return ans

                    
