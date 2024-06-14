class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        ans = []
        atlantic_reachable = set()
        pacific_reachable = set()
        def findRainCells(row,col,reachable):
            reachable.add((row,col))
            for(x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row,new_col = row+x,col+y
                if new_row<0 or new_row >= n or new_col<0 or new_col>=m:
                    continue
                if (new_row,new_col) in reachable:
                    continue
                if heights[row][col]>heights[new_row][new_col]:
                    continue
                findRainCells(new_row,new_col,reachable)
        for i in range(n):
            findRainCells(i,0,pacific_reachable)
            findRainCells(i,m-1,atlantic_reachable)
        for i in range(m):
            findRainCells(0,i,pacific_reachable)
            findRainCells(n-1,i,atlantic_reachable)
        return list(atlantic_reachable.intersection(pacific_reachable))
