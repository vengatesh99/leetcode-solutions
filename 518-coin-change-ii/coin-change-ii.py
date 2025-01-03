class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1)]*(len(coins)+1)
        n = len(coins)
        for i in range(n):
            dp[i][0] = 1
        for i in range(n):
            for j in range(1,amount+1):
                if coins[i]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-coins[i]]+dp[i][j]
        return dp[n][amount]


