class Solution:
    def isSafe(self,X,Y,n,m):
        return X>=0 and X<n and Y>=0 and Y<m

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        minutes = -1
        fresh = 0
        queue = deque()
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        queue.append((-1,-1))
        while queue:
            row,col = queue.popleft()
            if row == -1:
                minutes+=1
                if queue:
                    queue.append((-1,-1))
            else:
                for x,y in directions:
                    if self.isSafe(row+x,col+y,n,m) and grid[row+x][col+y] == 1:
                        # visited.add((row+x,col+y))
                        queue.append((row+x,col+y))
                        grid[row+x][col+y] = 2
                        fresh-=1
        
        return minutes if fresh == 0 else -1