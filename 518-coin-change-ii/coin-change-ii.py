class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(index,remaining):
            if remaining == 0:
                return 1
            if index == len(coins):
                return 0
            if(index,remaining) in memo:
                return memo[(index,remaining)]
            numWays = 0
            if coins[index] > remaining:
                numWays = dp(index+1,remaining)
            else:
                numWays = dp(index,remaining - coins[index]) + dp(index+1, remaining)
            memo[(index,remaining)] = numWays
            return numWays
        ans = dp(0,amount)
        return ans