class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        row_mat = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    row_mat[i][j] = mat[i][j]
                    continue
                row_mat[i][j] = row_mat[i-1][j]+mat[i][j]
        for i in range(n):
            for j in range(m):
                r_min = -1
                if i-k-1>=0:
                    r_min = i-k-1
                r_max = min(i+k,n-1)
                s = 0
                for y in range(max(0,j-k),min(j+k+1,m)):
                    s += row_mat[r_max][y]
                    if r_min>-1:
                        s-=row_mat[r_min][y]
                ans[i][j] = s
        return ans
