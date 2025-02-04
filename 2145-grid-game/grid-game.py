class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        preRow1,preRow2 = grid[0].copy(),grid[1].copy()
        n = len(grid[0])
        for i in range(1,n):
            preRow1[i]+=preRow1[i-1]
            preRow2[i]+=preRow2[i-1]
        ans = float("inf")
        for i in range(n):
            first = preRow1[-1]-preRow1[i]
            second = preRow2[i-1] if i>0 else 0
            ans = min(ans,max(first,second))
        return ans
        
