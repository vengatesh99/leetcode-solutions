class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        ans = float("-inf")
        count0 = 0
        while r<len(nums):
            if not nums[r]:
                count0+=1
            while count0>k:
                if nums[l] == 0:
                    count0-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans