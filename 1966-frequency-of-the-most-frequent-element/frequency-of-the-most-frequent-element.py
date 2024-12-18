class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        nums.sort()
        n = len(nums)
        ans = 1
        curr = 0
        while right < n:
            curr += nums[right]
            while (right - left +1)*nums[right] - curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans,right-left+1)
            right +=1
        return ans