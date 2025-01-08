class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        count = 0
        ones = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ones+=1
        def dfs(row,col,visit):
            if row < 0 or col < 0 or row == R or col == C or (row,col) in visit or not grid[row][col]:
                return 0
            visit.add((row,col))
            return grid[row][col]+dfs(row+1,col,visit)+dfs(row-1,col,visit)+dfs(row,col+1,visit)+dfs(row,col-1,visit)
        visit = set()
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0 or i == R-1 or j == C-1:
                    if grid[i][j] == 1:
                        count+=dfs(i,j,visit)
        print(ones,count)
        return ones-count