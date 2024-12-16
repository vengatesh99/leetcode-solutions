class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [0]*n
        stack.append(0)
        for i in range(1,n):
            while stack and nums[i] <= nums[stack[-1]]:
                ind = stack.pop()
                nextSmall = i
                ele = nums[ind]
                prevSmall = stack[-1] if stack else -1
                rg = nextSmall - prevSmall -1
                ans[rg-1] = max(ans[rg-1],ele)
            stack.append(i)
        print(ans,stack)
        while stack:
            ind = stack.pop()
            nextSmall = n
            ele = nums[ind]
            prevSmall = stack[-1] if stack else -1
            rg = nextSmall - prevSmall -1
            ans[rg-1] = max(ans[rg-1],ele)
        for i in range(n-2, -1, -1):                             # update non-touched windows using result for larger windows
            ans[i] = max(ans[i], ans[i+1])
        return ans
                
                
