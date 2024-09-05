# 1. Perform DFS
# 2. Store the distinct islands in a list
# 3. While storing, iterate the existing list to check if there is same islands

class Solution:
    def __init__(self):
        self.directions = [(-1,0),(0,-1),(0,1),(1,0)]
    def isSafe(self,x,y,n,m,grid):
        return (x>=0 and x<n) and (y>=0 and y<m) and grid[x][y] == 1
    def dfs(self,i,j,n,m,grid,island):
        if not self.isSafe(i,j,n,m,grid):
            return
        # if grid[i][j] == 0:
        #     return
        island.append([i,j])
        grid[i][j] = 0
        for x,y in self.directions:
            self.dfs(i+x,j+y,n,m,grid,island)
    
    def isSame(self,new_island,old_island):
        Xdiff,Ydiff = abs(new_island[0][0]-old_island[0][0]), abs(new_island[0][1]-old_island[0][1])
        for i in range(1,len(new_island)):
            if Xdiff != abs(new_island[i][0]-old_island[i][0]) or Ydiff !=  abs(new_island[i][1]-old_island[i][1]):
                return False
        return True

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        islands = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island = []
                    self.dfs(i,j,n,m,grid,island)
                    # print(island)
                    if len(islands) == 0:
                        islands.append(island)
                        print(island)
                        continue
                    flag = False
                    for old_island in islands:
                        if len(island) == len(old_island):
                            if self.isSame(island,old_island):
                                flag = True
                                break
                    if not flag:
                        islands.append(island)
        # print(islands)
        return len(islands)

                        
                