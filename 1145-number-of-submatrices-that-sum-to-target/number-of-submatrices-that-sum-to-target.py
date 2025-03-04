class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n,m = len(matrix),len(matrix[0])
        pm = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                pm[i][j] = pm[i-1][j]+pm[i][j-1]-pm[i-1][j-1]+matrix[i-1][j-1]
        
        count = 0
        for r1 in range(1,n+1):
            for r2 in range(r1,n+1):
                hm = {0:1}
                for c in range(1,m+1):
                    cs = pm[r2][c]-pm[r1-1][c]
                    count+=hm.get(cs-target,0)
                    hm[cs] = hm.get(cs,0)+1
        return count
                