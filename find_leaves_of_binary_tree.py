# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.leafList = [[]]

    def recursiveHelper(self, node):
        if node.left is None and node.right is None:
            self.leafList[0].append(node.val)
            return 1

        rightLevel = 0
        leftLevel = 0

        if node.right is not None:
            rightLevel = self.recursiveHelper(node.right)

        if node.left is not None:
            leftLevel = self.recursiveHelper(node.left)

        currLevel = max(leftLevel, rightLevel)

        if currLevel >= len(self.leafList):
            self.leafList.append([])

        self.leafList[currLevel].append(node.val)
        return currLevel + 1

    def findLeaves(self, root: TreeNode):
        if root is None:
            return []

        self.recursiveHelper(root)
        return self.leafList
