class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse) -> int:
        houseStack = []
        maxHeight = warehouse[0]

        for h in warehouse:
            maxHeight = min(maxHeight, h)
            houseStack.append(maxHeight)

        boxStack = sorted(boxes, reverse=True)

        boxesInserted = 0
        currBoxIndex = len(boxStack) - 1
        while len(houseStack) > 0 and currBoxIndex >= 0:
            currHouse = houseStack.pop()
            currBox = boxStack[currBoxIndex]

            if currBox <= currHouse:
                boxesInserted += 1
                currBoxIndex -= 1

        return boxesInserted
