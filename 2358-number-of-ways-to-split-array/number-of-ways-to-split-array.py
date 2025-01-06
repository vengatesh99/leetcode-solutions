class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = [0 for _ in range(len(nums))]
        prefix[0] = nums[0]
        ans = 0

        for i in range(len(nums)-1):
            prefix[i] = prefix[i-1]+nums[i] if i>0 else nums[i]
            if prefix[i]>=total-prefix[i]:
                ans+=1
        return ans