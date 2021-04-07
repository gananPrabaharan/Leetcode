class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Coordinates for moving in each direction - N, E, S, W
        directionOrder = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        dirIndex = 0  # Keeps track of what direction we are currently facing (maps back to directionOrder)
        position = [0, 0]  # Current position (start at origin)

        # Perform 4 rounds of instructions, and check whether we are back at origin (will be facing N after 4 iterations)
        for _ in range(4):
            for i in instructions:
                if i == "G":
                    position[0] += directionOrder[dirIndex][0]
                    position[1] += directionOrder[dirIndex][1]
                elif i == "L":
                    # Move backwards in directionOrder
                    # Modulo to keep us within (0, 3) range inclusive
                    dirIndex -= 1
                    dirIndex %= 4
                elif i == "R":
                    # Move backwards in directionOrder
                    # Modulo to keep us within (0, 3) range inclusive
                    dirIndex += 1
                    dirIndex %= 4
                else:
                    raise ValueError

        # Make sure we are back at origin
        return position[0] == 0 and position[1] == 0
