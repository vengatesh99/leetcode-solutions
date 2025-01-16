class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        reachable = set()
        seen = set()
        m,n = len(board),len(board[0])
        def dfs(i,j):
            seen.add((i,j))
            if i<0 or i==m or j<0 or j==n:
                return
            if board[i][j] == "X":
                return
            reachable.add((i,j))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for d in directions:
                if (i+d[0],j+d[1]) not in seen:
                    dfs(i+d[0],j+d[1])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in reachable:
                    board[i][j] = "X"
            


        