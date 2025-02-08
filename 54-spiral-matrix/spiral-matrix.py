class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit = set()
        result = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]] #R,D,L,U
        n,m = len(matrix),len(matrix[0])
        ind = 0
        def traverse(row,col,move):
            if min(row,col)<0 or row==n or col == m or (row,col) in visit:
                return
            result.append(matrix[row][col])
            visit.add((row,col))
            if move == "R":
                traverse(row,col+1,"R")
                traverse(row+1,col,"D")
            elif move == "D":
                traverse(row+1,col,"D")
                traverse(row,col-1,"L")
            elif move == "L":
                traverse(row,col-1,"L")
                traverse(row-1,col,"U")
            else:
                traverse(row-1,col,"U")
                traverse(row,col+1,"R")
            # traverse(row,col+1)
            # traverse(row+1,col)
            # traverse(row,col-1)
            # traverse(row-1,col)
        traverse(0,0,"R")
        return result
