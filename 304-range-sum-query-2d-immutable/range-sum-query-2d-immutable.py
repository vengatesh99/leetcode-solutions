class NumMatrix:

    def calculateArea(self,area,matrix):
        row,col = len(area),len(area[0])
        for i in range(1,row):
            for j in range(1,col):
                if i == 1 and j == 1:
                    area[i][j] = matrix[i-1][j-1]
                elif i == 1:
                    area[i][j] = area[i][j-1]+matrix[i-1][j-1]
                elif j == 1:
                    area[i][j] = area[i-1][j]+matrix[i-1][j-1]
                else:
                    area[i][j] = area[i-1][j]+area[i][j-1]-area[i-1][j-1]+matrix[i-1][j-1]
        print(area)

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.r = len(matrix)
        self.c = len(matrix[0])
        self.area = [[0 for _ in range(self.c+1)] for _ in range(self.r+1)]
        self.calculateArea(self.area,self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.area[row2+1][col2+1]-self.area[row1][col2+1]-(self.area[row2+1][col1]-self.area[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)