class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        visited = set()
        def dp(i,j,moves):
            if moves > maxMove:
                return 0
            if i>=m or i<0 or j<0 or j>=n:
                return 1
            # if (i,j) in visited:
            #     return 0
            if (i,j,moves) in memo:
                return memo[(i,j,moves)]
            # visited.add((i,j))
            paths = dp(i+1,j,moves+1)+dp(i-1,j,moves+1)+dp(i,j+1,moves+1)+dp(i,j-1,moves+1)
            paths = paths % (10**9 + 7)
            memo[(i,j,moves)] = paths
            # print(i,j,paths)
            # memo[(i,j)] = paths
            # return memo[(i,j)]
            return paths
        
        return dp(startRow,startColumn,0)
            