class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        matrix_copy = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        max_len = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix_copy[i][j] = matrix[i][j]
                    max_len = max(max_len,matrix_copy[i][j])
                    continue
                elif matrix[i][j] == 0:
                    continue
                matrix_copy[i][j] = min(matrix_copy[i][j-1],matrix_copy[i-1][j-1],matrix_copy[i-1][j])+1
                
                max_len = max(max_len,matrix_copy[i][j])
        print(matrix_copy)
        return max_len**2

        