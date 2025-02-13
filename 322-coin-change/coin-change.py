class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(target):
            if target == 0:
                return 0
            if target < 0:
                return float("inf")
            if target in memo:
                return memo[target]
            req = float("inf")
            for coin in coins:
                req = min(req,1+dp(target-coin))
            # if req != float("inf"):
            memo[target] = req
            return req
        c = dp(amount)
        return c if c!=float("inf") else -1