class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        count = 0
        for i in range(n):
            while stack and height[stack[-1]]<=height[i]:
                top = stack.pop()
                if stack:
                    h = min(height[i],height[stack[-1]]) - height[top]
                    width = i - (stack[-1]+1)
                    count += width*h
            stack.append(i)
        return count