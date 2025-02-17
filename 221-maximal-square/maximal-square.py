class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        length = 0
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            length = max(length,dp[i][0])
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
            length = max(length,dp[0][j])
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == "0": 
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                length = max(length,dp[i][j])
        return length**2