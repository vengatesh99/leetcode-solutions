class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i,n = 0,len(heights)
        stack = []
        maxArea = 0
        while i<n:
            if not stack or heights[i]>=stack[-1][1]:
                stack.append([i,heights[i]])
            else:
                t = i
                while stack and stack[-1][1]>heights[i]:
                    t,h = stack.pop()
                    maxArea = max(maxArea,(i-t)*h)
                stack.append([t,heights[i]])
            i+=1
        while stack:
            t,h = stack.pop()
            maxArea = max(maxArea, (n-t)*h)
        return maxArea
                
                    