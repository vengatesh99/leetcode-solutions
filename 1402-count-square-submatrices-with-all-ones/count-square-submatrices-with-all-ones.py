import copy
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = copy.deepcopy(matrix)
        n,m = len(matrix),len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    ans+=dp[i][j]
                    continue
                if dp[i][j]:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans+=dp[i][j]

        return ans 