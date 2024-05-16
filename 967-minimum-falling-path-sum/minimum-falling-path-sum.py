class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j==0:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                elif j == m-1:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1],dp[i-1][j-1])
        return min(dp[n-1])