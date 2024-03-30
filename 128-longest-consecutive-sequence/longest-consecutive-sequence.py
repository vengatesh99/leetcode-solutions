class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        map = {}
        i,ans = 0,1
        if len(nums) == 0:
            return 0
        while i<n:
            if nums[i]-1 not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] = map[nums[i]-1]+1
                ans = max(ans,map[nums[i]])
            i+=1
        
        return ans