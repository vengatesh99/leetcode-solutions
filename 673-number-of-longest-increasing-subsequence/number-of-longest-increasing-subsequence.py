class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        n = len(nums)
        hashmap = defaultdict(int)
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    newlen = 1+dp[j][0]
                    if newlen>dp[i][0]:
                        dp[i] = [newlen,dp[j][1]]
                    elif newlen == dp[i][0]:
                        dp[i][1] += dp[j][1]
        # print(dp)
        for l,v in dp:
            hashmap[l]+=v
        # print(hashmap)
        return hashmap[max(hashmap.keys())]
                
                    