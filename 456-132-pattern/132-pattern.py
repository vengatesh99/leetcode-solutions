class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        stack.append((nums[0],nums[0]))
        curMin = nums[0]
        for i in range(1,n):
            while stack and nums[i]>=stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1] < nums[i]:
                return True
            stack.append((nums[i],curMin))
            curMin = min(curMin,nums[i])
        return False
                

