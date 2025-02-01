class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        indexMap = {i+1:[] for i in range(len(arr))}
        m,n = len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                indexMap[mat[i][j]] = [i,j]
        row = [0]*m
        col = [0]*n
        for i in range(len(arr)):
            paintR,paintC = indexMap[arr[i]]
            row[paintR]+=1
            col[paintC]+=1
            if row[paintR] == n or col[paintC] == m:
                return i
        return len(arr)

