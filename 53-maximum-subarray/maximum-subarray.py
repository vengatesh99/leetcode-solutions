class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        for n in nums:
            if curr_sum + n > n:
                curr_sum+=n
            else:
                curr_sum = n
            max_sum = max(max_sum,curr_sum)
        return max_sum