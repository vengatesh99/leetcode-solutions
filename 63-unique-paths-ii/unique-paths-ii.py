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
            # nonlocal paths
            visit.add((row,col))
            if row == m-1 and col == n-1:
                return 1
            if (row,col) in memo:
                return memo[(row,col)]
            paths = 0
            for r,c in directions:
                newR,newC = row+r,col+c
                if  min(newR,newC)<0 or newR==m or newC == n or (newR,newC) in visit or obstacleGrid[newR][newC]:
                    continue
                paths+=dfs(newR,newC)
                visit.remove((newR,newC))
            memo[(row,col)] = paths
            return memo[(row,col)]
        return dfs(0,0)

            