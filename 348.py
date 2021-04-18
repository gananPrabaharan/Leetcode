class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.columnSums = [0] * n
        self.rowSums = [0] * n
        self.dimension = n
        self.posDiag = 0
        self.negDiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            value = -1
        else:
            value = 1

        self.rowSums[row] += value
        self.columnSums[col] += value

        if row == col:
            self.posDiag += value

        if row + col == self.dimension - 1:
            self.negDiag += value

        target = value * self.dimension
        if self.rowSums[row] == target:
            return player
        if self.columnSums[col] == target:
            return player
        if self.posDiag == target:
            return player
        if self.negDiag == target:
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)