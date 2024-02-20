class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_list(house):
            dp = [0]*len(house)
            dp[0] = house[0]
            for i in range(1,len(dp)):
                if i<=1:
                    dp[i] = max(house[i],dp[i-1])
                else:
                    dp[i] = max(dp[i-1],dp[i-2]+house[i])
            return dp[-1]
        if len(nums)<=1:
            return max(nums)
        return max(rob_list(nums[1:]),rob_list(nums[0:len(nums)-1]))