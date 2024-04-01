class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = sum = nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            ans = max(ans,math.ceil(sum/(i+1)))
    
        return ans