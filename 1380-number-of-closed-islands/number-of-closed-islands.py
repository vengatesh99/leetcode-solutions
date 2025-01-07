class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        def dfs(row,col,visited):
            if (row,col) in visited:
                return 1
            if row==n or col == m or row<0 or col<0:
                return 0
            if grid[row][col] == 1:
                return 1
            visited.add((row,col))
            if dfs(row+1,col,visited) and dfs(row-1,col,visited) and dfs(row,col+1,visited) and dfs(row,col-1,visited):
                grid[row][col] = 2
                return 1
            return 0
        ans = 0
        for i in range(n):
            for j in range(m):
                visited = set()
                if grid[i][j] == 0 and dfs(i,j,visited):
                    ans+=1
        return ans
            
