import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valIndexDict = {}
        self.valList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valIndexDict:
            return False

        self.valList.append(val)
        self.valIndexDict[val] = len(self.valList) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valIndexDict:
            return False

        # Swap last element with value we want to remove
        valIndex = self.valIndexDict[val]

        lastElement = self.valList[-1]
        self.valList[-1] = val
        self.valList[valIndex] = lastElement
        self.valIndexDict[lastElement] = valIndex

        # Pop from valList to get rid of val
        self.valList.pop()

        # Remove value from hashmap
        del self.valIndexDict[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randIndex = random.randint(0, len(self.valList) - 1)
        return self.valList[randIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()