class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                right = i - stack[-1]
                ind = stack.pop()
                left = ind - ((stack[-1]+1) if stack else 0)
                ans[ind] = right+left
            stack.append(i)
        while stack:
            right = len(nums) - stack[-1]
            ind = stack.pop()
            left = ind - ((stack[-1]+1) if stack else 0)
            ans[ind] = left+right
        return ans