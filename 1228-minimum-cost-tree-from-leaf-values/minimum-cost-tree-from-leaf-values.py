class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        memo = {}
        def dp(i,j):
            if i>=j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            cost = float("inf")
            for k in range(i,j):
                cost = min(cost,dp(i,k)+dp(k+1,j)+max(arr[i:k+1])*max(arr[k+1:j+1]))
            memo[(i,j)] = cost
            return cost

        return dp(0,len(arr)-1)