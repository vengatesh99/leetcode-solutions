class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        hash_map = {}
        def dp(row,col):
            if row<0 or col<0:
                return 0
            if row == 0 and col ==0:
                return 1 if obstacleGrid[row][col]==0 else 0
            if obstacleGrid[row][col] == 1:
                return 0
            if (row,col) in hash_map:
                return hash_map[(row,col)]
            path = dp(row-1,col)+dp(row,col-1)
            hash_map[(row,col)] = path
            return path
        n,m = len(obstacleGrid),len(obstacleGrid[0])
        if n==1 and m == 1:
            return 1 if obstacleGrid[n-1][m-1]==0 else 0
        return dp(n-1,m-1)