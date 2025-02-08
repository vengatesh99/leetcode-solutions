class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = deque()
        n = len(matrix)
        m = len(matrix[0])
        visit = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    queue.append((i,j))
        while queue:
            r,c = queue.popleft()
            for i in range(n):
                matrix[i][c] = 0
            for i in range(m):
                matrix[r][i] = 0
        return matrix
            
        