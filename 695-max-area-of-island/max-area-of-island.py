class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(row,col):
            if min(row,col)<0 or row == n or col == m or visit[row][col] or not grid[row][col]:
                return 0
            visit[row][col] = True
            area = 1+dfs(row+1,col)+dfs(row,col+1)+dfs(row-1,col)+dfs(row,col-1)
            return area
        ans = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visit[i][j]:
                    ans = max(ans,dfs(i,j))
        return ans
            