class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        directions = [-1,0,1]
        memo = {}
        def dp(i,j1,j2):
            if j1<0 or j1 == m or j2<0 or j2==m:
                return 0
            if j1 == j2:
                return grid[i][j1]
            if i==n-1:
                return grid[i][j1]+grid[i][j2]
            if(i,j1,j2) in memo:
                return memo[(i,j1,j2)]
            psum = 0
            for c1 in directions:
                for c2 in directions:
                    psum=max(psum,grid[i][j1]+grid[i][j2]+dp(i+1,j1+c1,j2+c2))
            memo[(i,j1,j2)] = psum
            return psum
        return dp(0,0,m-1)

            
