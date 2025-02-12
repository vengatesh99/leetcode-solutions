class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1 for _ in pairs]
        pairs.sort()
        for i in range(1,len(pairs)):
            for j in range(i-1,-1,-1):
                if pairs[j][1]<pairs[i][0]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)