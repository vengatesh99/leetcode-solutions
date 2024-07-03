class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.rowSum = [[0 for _ in range(n)] for _  in range(2)]
        self.colSum = [[0 for _ in range(n)] for _  in range(2)]
        self.diagSum1 = [0 for _ in range(2)]
        self.diagSum2 = [0 for _ in range(2)]
    def checkWinner(self,diagSum1,diagSum2,row,col,player):
        # for i in range(self.n):
        #     rowSum = 0
        #     for j in range(self.n):
        #         rowSum+=self.board[i][j]
        #         if i == j:
        #             diagSum1+=self.board[i][j]
        #         if i+j == self.n:
        #             diagSum2+=self.board[i][j]
        if row == col:
            self.diagSum1[player-1]+=player
        if row+col == self.n-1:
            self.diagSum2[player-1]+=player

        self.rowSum[player-1][row] += player
        self.colSum[player-1][col] += player


        if self.rowSum[player-1][row] == player*self.n or self.colSum[player-1][col] == player*self.n:
            return player
        if self.diagSum1[player-1] == player*self.n or self.diagSum2[player-1]==player*self.n:
            return player
           
        return -1
        # for j in range(self.n):
        #     colSum = 0
        #     for i in range(self.n):
        #         colSum+=self.board[i][j]
        #     if colSum == 1*self.n:
        #         return 1
        #     if colSum == 2*self.n:
        #         return 2
        # return -1


    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        winner = self.checkWinner(0,0,row,col,player)
        if winner == 1 or winner == 2:
            return winner
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)