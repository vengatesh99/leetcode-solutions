class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ind = set()
        ans = []
        n = len(heights)
        stack = []
        i = 0
        for i in range(n):
            while stack and heights[stack[-1]]<=heights[i]:
                ind.add(stack[-1])
                stack.pop()
            stack.append(i)
        for i in range(n):
            if i not in ind:
                ans.append(i)
        return ans

