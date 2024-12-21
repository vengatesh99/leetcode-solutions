class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(idx, sum):
            if (idx,sum) in memo:
                return memo[(idx,sum)]
            if idx == n:
                return sum == target
            val = dp(idx+1,sum+nums[idx]) + dp(idx+1,sum-nums[idx])
            memo[(idx,sum)] = val
            return val
        return dp(0,0)

