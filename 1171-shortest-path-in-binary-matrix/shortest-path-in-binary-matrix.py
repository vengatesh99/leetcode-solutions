class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append((0,0,0))
        directions = [(0,1),(0,-1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        seen = set()
        steps = 0
        reachable = False
        while q:
            r,c,d = q.popleft()
            steps = d
            if r == n-1 and c==n-1:
                reachable = True
                break
            for dx,dy in directions:
                nr,nc = r+dx,c+dy
                if min(nr,nc)>=0 and max(nr,nc)<n and (nr,nc) not in seen and not grid[nr][nc]:
                    seen.add((nr,nc))
                    q.append((nr,nc,d+1))
        return steps+1 if reachable else -1
            

