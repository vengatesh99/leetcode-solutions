class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        # paths = 0
        visit = set()
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0
        directions = [[0,1],[1,0]]
        memo = {}
        def dfs(row,col):
            if row == m or col == n or obstacleGrid[row][col]:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if (row,col) in memo:
                return memo[(row,col)]
            paths = 0
            for r,c in directions:
                newR,newC = row+r,col+c
                paths+=dfs(newR,newC)
            memo[(row,col)] = paths
            return memo[(row,col)]
        return dfs(0,0)

            