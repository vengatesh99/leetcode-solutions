class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = []
        q.append((grid[0][0],0,0))
        visit = set()
        n = len(grid)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = float("inf")
        while q:
            t,row,col = heapq.heappop(q)
            if (row,col) in visit:
                continue
            if row == n-1 and col == n-1:
                ans = min(ans,t)
            visit.add((row,col))
            for r,c in directions:
                newR,newC = row+r,col+c
                if min(newR,newC)<0 or max(newR,newC)>=n or (newR,newC) in visit:
                    continue
                heapq.heappush(q,(max(t,grid[newR][newC]),newR,newC))
        return ans
            