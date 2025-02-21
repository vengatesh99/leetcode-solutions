class Solution:
    def largestRectangleHistogram(self,heights):
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
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        maxArea = 0
        matrix = [[0 if matrix[i][j] == "0" else 1 for j in range(m)] for i in range(n)]
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or not matrix[i][j]:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = 1+dp[i-1][j]
        for row in dp:
            maxArea = max(maxArea,self.largestRectangleHistogram(row))
        return maxArea

        