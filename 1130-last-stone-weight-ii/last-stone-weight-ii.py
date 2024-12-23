class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        sum_weights = sum(stones)
        half_weight = sum_weights // 2
        memo = {}
        def dp(idx,target):
            if idx == n or target == 0:
                return 0
            if (idx,target) in memo:
                return memo[(idx,target)]
            if target - stones[idx] < 0:
                return dp(idx+1,target)
            ans = max(stones[idx] + dp(idx+1,target-stones[idx]),dp(idx+1,target))
            memo[(idx,target)] = ans
            return memo[(idx,target)]
        closest_half = dp(0,half_weight)
        return sum_weights - 2*closest_half