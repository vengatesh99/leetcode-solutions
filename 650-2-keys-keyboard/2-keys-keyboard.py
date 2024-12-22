class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dp(curr,n,clipboard):
            if curr == n:
                return 0
            if curr > n:
                return 1000
            if (curr,clipboard) in memo:
                return memo[(curr,clipboard)]
            opt1 = 2+dp(curr*2,n,curr)
            opt2 = 1+dp(curr+clipboard,n,clipboard)
            memo[(curr,clipboard)] = min(opt1,opt2)
            return memo[(curr,clipboard)]
        if n == 1:
            return 0
        return 1+dp(1,n,1)