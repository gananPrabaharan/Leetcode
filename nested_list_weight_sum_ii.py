# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def __init__(self):
        self.maxDepth = 0
        self.intTuples = []

    def dfs(self, nestedList, depth):
        # Update max depth if needed
        self.maxDepth = max(self.maxDepth, depth)

        for element in nestedList:
            if element.isInteger():
                self.intTuples.append((depth, element.getInteger()))
            else:
                self.dfs(element.getList(), depth + 1)

    def depthSumInverse(self, nestedList) -> int:
        if nestedList is None:
            return 0

        # Depth first search to identify all integers and their weights
        self.dfs(nestedList, 1)

        weightSum = 0
        for depth, integer in self.intTuples:
            weight = self.maxDepth - depth + 1
            weightSum += weight * integer

        return weightSum
