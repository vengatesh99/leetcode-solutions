class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = {}
        def dp(ind):
            if ind == n:
                return 0
            if ind in memo:
                return memo[ind]
            num = 0
            s = 0
            partition = 0
            for i in range(ind,min(ind+k,n)):
                num = max(num,arr[i])
                s = max(s,(i-ind+1)*(num)+dp(i+1))
            memo[ind] = s
            return s
        ans = dp(0)
        return ans