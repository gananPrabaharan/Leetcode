class Solution:
    def __init__(self):
        self.sum = 0

    def listIterator(self, nestedInteger, depth):
        for element in nestedInteger:
            if element.isInteger():
                self.sum += depth * element.getInteger()
            self.listIterator(element.getList(), depth + 1)

    def depthSum(self, nestedList):
        self.listIterator(nestedList, 1)
        return self.sum
