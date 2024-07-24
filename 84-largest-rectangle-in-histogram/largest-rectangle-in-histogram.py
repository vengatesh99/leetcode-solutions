class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append((heights[0],0))
        n = len(heights)
        maxArea = 0
        for i in range(1,n):
            last_ind = i
            while len(stack)>0 and stack[-1][0]>heights[i]:
                maxArea = max(maxArea,(i-stack[-1][1])*stack[-1][0])
                _,last_ind = stack.pop()
            stack.append((heights[i],last_ind))
        while stack:
            height,left = stack.pop()
            maxArea = max(maxArea,(n-left)*height)
        return maxArea
            
