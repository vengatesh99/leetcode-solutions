class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        # memo = {}
        # def dp(amt,idx):
        #     if amt == 0:
        #         return 1
        #     if idx == n or amt<0:
        #         return 0
        #     if(amt,idx) in memo:
        #         return memo[(amt,idx)]
        #     # ways = 0
        #     ways = dp(amt-coins[idx],idx) + dp(amt,idx+1)
        #     memo[(amt,idx)] = ways
        #     return ways
        # w = dp(amount,0)
        # return w

        #Tabulation
        #1. Base Case
        #2. Identify States
        #3. Copy the recursion

        dp = [[0 for i in range(0,amount+1)] for _ in range(N+1)]
        m,n = len(dp),len(dp[0])
        for i in range(m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if j>=coins[i-1]:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][amount]
    