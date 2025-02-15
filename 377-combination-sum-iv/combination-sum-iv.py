class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(t):
            if t<0:
                return 0
            if t == 0:
                return 1
            if t in memo:
                return memo[t]
            ways = 0
            for num in nums:
                ways += dp(t-num)
            memo[t] = ways
            return ways
        return dp(target)