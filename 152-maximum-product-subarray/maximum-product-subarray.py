class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        max_prod = float("-inf")
        curr_min = 1
        prev_min,prev_max = 1,1
        for n in nums:
            curr_max = max(curr_max*n,n,prev_min*n)
            curr_min = min(curr_min*n,n,prev_max*n)
            prev_min = curr_min
            prev_max = curr_max
            max_prod = max(max_prod,curr_max)
        return max_prod