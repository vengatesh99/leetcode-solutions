class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = set()
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.add((i,j))
        for row, col in zeroes:
            for j in range(n):
                matrix[row][j] = 0
            for i in range(m):
                matrix[i][col] = 0
        

        