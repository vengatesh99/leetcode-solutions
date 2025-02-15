class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # memo = {}
        # def dp(t):
        #     if t<0:
        #         return 0
        #     if t == 0:
        #         return 1
        #     if t in memo:
        #         return memo[t]
        #     ways = 0
        #     for num in nums:
        #         ways += dp(t-num)
        #     memo[t] = ways
        #     return ways
        # return dp(target)

        #Tabulation
        # 1. Base case
        # 2. initiliaze i,j
        # 3. Convert recurrence to forloop statements
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        M = len(dp)
        for i in range(M):
            for num in nums:
                if num<=i:
                    dp[i]+=dp[i-num]
        return dp[target]
                
        