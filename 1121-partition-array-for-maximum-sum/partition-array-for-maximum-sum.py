class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # memo = {}
        # def dp(ind):
        #     if ind == n:
        #         return 0
        #     if ind in memo:
        #         return memo[ind]
        #     num = 0
        #     s = 0
        #     partition = 0
        #     for i in range(ind,min(ind+k,n)):
        #         num = max(num,arr[i])
        #         s = max(s,(i-ind+1)*(num)+dp(i+1))
        #     memo[ind] = s
        #     return s
        # ans = dp(0)
        dp = [0 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            s = 0
            num = 0
            for j in range(i,min(i+k,n)):
                num = max(num,arr[j])
                s = max(s,(j-i+1)*(num) + dp[j+1])
            dp[i] = s
        return dp[0]

        return ans