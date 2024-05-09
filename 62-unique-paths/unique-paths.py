class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hash_map = {}
        def dp(row,col):
            if row == 0 and col == 0:
                return 1
            if row<0 or col<0:
                return 0
            if (row,col) in hash_map:
                return hash_map[(row,col)]
            hash_map[(row,col)] = dp(row,col-1)+dp(row-1,col)
            return hash_map[(row,col)]
        return dp(m-1,n-1)