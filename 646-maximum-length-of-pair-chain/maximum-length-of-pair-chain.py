class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[0])
        memo = {}
        def dp(index):
            if index == 0:
                return 1
            if index in memo:
                return memo[index]
            ans = 1
            for i in range(index):
                if pairs[i][1] < pairs[index][0]:
                    ans = max(ans, 1+dp(i))
            memo[index] = ans
            return ans
        ans = 1
        for i in range(1,len(pairs)):
            ans = max(ans,dp(i))
        return ans
                