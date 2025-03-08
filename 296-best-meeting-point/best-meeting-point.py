class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        midRow = rows[len(rows)//2]
        cols.sort()
        midCol = cols[len(cols)//2]
        def findDist(mid,l):
            d = 0
            for point in l:
                d+=abs(point-mid)
            return d
        return findDist(midRow,rows)+findDist(midCol,cols)