class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        q = [(0,0,0)]
        while q:
            diff,cx,cy = heapq.heappop(q)
            if (cx,cy) in visit:
                continue
            visit.add((cx,cy))
            if cx == rows-1 and cy == cols-1:
                return diff
            for dx,dy in directions:
                newX,newY = cx+dx,cy+dy
                if newX<0 or newX ==rows or newY<0 or newY==cols or (newX,newY) in visit:
                    continue
                newDiff = max(diff,abs(heights[cx][cy]-heights[newX][newY]))
                heapq.heappush(q,(newDiff,newX,newY))
        return -1
            
                