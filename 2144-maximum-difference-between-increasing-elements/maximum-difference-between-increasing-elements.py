class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minEle = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>minEle:
                ans = max(ans,nums[i]-minEle)
            minEle = min(minEle,nums[i])
        return ans