class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        houses = [0]*len(nums)
        houses[0] = nums[0]
        maxAmt = houses[0]
        if n==1:
            return maxAmt
        houses[1] = max(nums[1],maxAmt)
        maxAmt = max(maxAmt,houses[1])
        for i in range(2,len(nums)):
            houses[i] = max(nums[i]+houses[i-2],houses[i-1])
            maxAmt = max(maxAmt,houses[i])
        return maxAmt
        