class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        m,n = len(grid),len(grid[0])
        minutes = 0
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    seen.add((i,j))
        while q:
            r,c,minutes = q.popleft()
            ans = minutes
            for dx,dy in directions:
                nr,nc = r+dx,c+dy
                if min(nr,nc)>=0 and nr<m and nc<n and (nr,nc) not in seen and grid[nr][nc] == 1:
                    seen.add((nr,nc))
                    q.append((nr,nc,minutes+1))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in seen:
                    return -1
        return ans
