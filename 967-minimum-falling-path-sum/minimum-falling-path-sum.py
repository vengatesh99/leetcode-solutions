class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        ans = float("inf")
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    leftD = float("inf") if j-1<0 else dp[i-1][j-1]
                    top = dp[i-1][j]
                    rightD = float("inf") if j+1 == m else dp[i-1][j+1]
                    dp[i][j] = min(leftD,top,rightD)+matrix[i][j]
        return min(dp[-1])
         
        