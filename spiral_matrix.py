class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []

        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up

        limitDict = {
            0: len(matrix[0]) - 1,
            1: len(matrix) - 1,
            2: 0,
            3: 1
        }

        multiplierList = [1, 1, -1, -1]


        numList = []
        direction = 0
        currCoord = [0, -1]
        matrixSize = len(matrix) * len(matrix[0])

        while len(numList) < matrixSize:
            index = (direction + 1) % 2
            multiplier = multiplierList[direction]

            currCoord[index] += multiplier

            currX = currCoord[0]
            currY = currCoord[1]

            numList.append(matrix[currX][currY])

            if currCoord[index] == limitDict[direction]:
                limitDict[direction] -= multiplier
                direction = (direction + 1) % 4

        return numList