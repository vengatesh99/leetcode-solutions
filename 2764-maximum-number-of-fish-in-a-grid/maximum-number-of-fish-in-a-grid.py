class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        fishes = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(row,col):
            if grid[row][col] == 0:
                return 0
            visit.add((row,col))
            s = grid[row][col]
            for r,c in directions:
                newR,newC = row+r,col+c
                if min(newR,newC)>=0 and newR<ROWS and newC<COLS and (newR,newC) not in visit:
                    s += dfs(newR,newC)
            return s

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] > 0 and (i,j) not in visit:
                    fishes = max(dfs(i,j),fishes)
        return fishes