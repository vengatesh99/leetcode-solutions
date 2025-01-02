class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dp(index):
            if index == 0:
                return [nums[0]]
            if index in memo:
                return memo[index]
            subsets = [nums[index]]
            for i in range(index):
                if nums[index] % nums[i] == 0:
                    newsubsets = dp(i) + [nums[index]]
                    if len(newsubsets) > len(subsets):
                        subsets = newsubsets
            memo[index] = subsets
            return memo[index]
        ans = []
        for i in range(len(nums)):
            subsetsAtI = dp(i)
            if len(ans) < len(subsetsAtI):
                ans = subsetsAtI
        return ans