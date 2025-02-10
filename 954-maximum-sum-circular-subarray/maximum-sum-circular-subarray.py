class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        min_sum = float("inf")
        curr_max = 0
        curr_min = 0
        n = len(nums)
        for i in range(n):
            if curr_max + nums[i]>nums[i]:
                curr_max+=nums[i]
            elif curr_max+nums[i]<=nums[i]:
                curr_max = nums[i]
            if curr_min+nums[i]<=nums[i]:
                curr_min+=nums[i]
            else:
                curr_min = nums[i]
            max_sum = max(max_sum,curr_max)
            min_sum = min(min_sum,curr_min)
        if min_sum == sum(nums):
            return max_sum
        return max(max_sum,sum(nums) - min_sum)