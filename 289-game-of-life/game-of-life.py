class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ones,zeroes = set(),set()
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        def countNeib(row,col,target):
            s = 0
            for r,c in directions:
                newR,newC = row+r,col+c
                if newR<0 or newC<0 or newR >= m or newC >= n:
                    continue
                if board[newR][newC] == target:
                    s+=1
            return s
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    ct = countNeib(i,j,1)
                    if ct <2 or ct>3:
                        zeroes.add((i,j))
                else:
                    ct = countNeib(i,j,1)
                    if ct == 3:
                        ones.add((i,j))
        for row,col in ones:
            board[row][col] = 1
        for row,col in zeroes:
            board[row][col] = 0
        