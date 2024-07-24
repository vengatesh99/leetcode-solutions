class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        i = 0
        n = len(nums)
        stack = []
        for i in range(2*n):
            i = i%n
            while stack and nums[stack[-1]]<nums[i]:
                if ans[stack[-1]] == -1:
                    ans[stack[-1]] = nums[i] 
                stack.pop()
            stack.append(i)
        return ans