class Vector2D:
    def __init__(self, vec):
        self.listStack = [vec]
        self.indexStack = [0]

    def jumpIn(self):
        if len(self.indexStack) == 0:
            return None

        # Determine next root level list
        while True:
            # Get latest list and associated index
            currList = self.listStack[-1]
            listIndex = self.indexStack[-1]

            if listIndex >= len(currList):
                self.listStack.pop()
                self.indexStack.pop()

                if len(self.indexStack) == 0:
                    return None

                # Increment parent list's index
                self.indexStack[-1] += 1
            elif type(currList[listIndex]) == list:
                self.listStack.append(currList[listIndex])
                self.indexStack.append(0)
            else:
                break

        return currList[listIndex]

    def next(self) -> int:
        nextVal = self.jumpIn()
        self.indexStack[-1] += 1

        return nextVal

    def hasNext(self) -> bool:
        nextVal = self.jumpIn()
        return nextVal is not None

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
