from collections import deque


class Solution:
    def __init__(self):
        self.board = None

    def checkValidity(self, row, col):
        if col < 0 or col == len(self.board[0]):
            return False
        if row < 0 or row == len(self.board):
            return False

        return True

    def checkCenter(self, row, col):
        if row == 0 or row == len(self.board) - 1 or col == 0 or col == len(self.board[0]) - 1:
            return False
        return True

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        currX = 0
        currY = 0

        if len(board) == 0 or len(board[0]) == 0:
            return
        self.board = board
        oSet = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    oSet.add((i, j))

        coordQueue = deque([])
        while len(oSet) > 0:
            currCoordinate = oSet.pop()
            coordQueue.append(currCoordinate)
            currRegion = set([currCoordinate])
            centerFlag = True

            while len(coordQueue) > 0:
                row, col = coordQueue.popleft()
                if not self.checkCenter(row, col):
                    centerFlag = False

                coordsToCheck = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for checkCoord in coordsToCheck:
                    if self.checkValidity(checkCoord[0], checkCoord[1]) and checkCoord in oSet:
                        coordQueue.append(checkCoord)
                        oSet.remove(checkCoord)
                        currRegion.add(checkCoord)

            if centerFlag:
                while len(currRegion) > 0:
                    regionRow, regionCol = currRegion.pop()
                    self.board[regionRow][regionCol] = "X"
