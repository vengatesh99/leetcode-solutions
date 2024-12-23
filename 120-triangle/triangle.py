class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def dp(row,col):
            if row == n:
                return 0
            if(row,col) in memo:
                return memo[(row,col)]
            path_sum = triangle[row][col] + min(dp(row+1,col),dp(row+1,col+1))
            memo[(row,col)] = path_sum
            return memo[(row,col)]
        return dp(0,0)