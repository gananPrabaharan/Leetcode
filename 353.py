from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.directions = {
            "U": (-1, 0),
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0)
        }

        self.snakeCoordSet = {(0, 0)}
        self.snakeQueue = deque([(0, 0)])
        self.height = height
        self.width = width

        self.foodCoords = []

        for i in range(len(food) - 1, -1, -1):
            coord = food[i]
            self.foodCoords.append((coord[0], coord[1]))

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        delta = self.directions[direction]
        head = self.snakeQueue[0]
        newPos = (head[0] + delta[0], head[1] + delta[1])

        if newPos[0] < 0 or newPos[0] == self.height:
            return -1
        if newPos[1] < 0 or newPos[1] == self.width:
            return -1
        print(newPos)
        if len(self.foodCoords) > 0 and newPos == self.foodCoords[-1]:
            self.foodCoords.pop()
        else:
            tail = self.snakeQueue.pop()
            self.snakeCoordSet.remove(tail)

        if newPos in self.snakeCoordSet:
            return -1

        self.snakeQueue.appendleft(newPos)
        self.snakeCoordSet.add(newPos)
        return len(self.snakeQueue) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
