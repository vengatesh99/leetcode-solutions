class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        row_count = [0]*ROWS
        col_count = [0]*COLS
        servers = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    row_count[i]+=1
                    col_count[j]+=1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] and (row_count[i]>1 or col_count[j]>1):
                    servers+=1
        return servers
        