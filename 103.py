from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrderBFS(self, root: TreeNode):
        if root is None:
            return []

        # Flag indicating direction of zigzag
        leftRight = True

        # Queue for current level nodes, nextQueue for next level nodes
        queue = deque([root])
        nextQueue = []

        zigzagNodes = []  # Result list
        currLevel = deque([])  # Values for current level nodes
        while len(queue) > 0:
            # Regular in-order BFS adding left to right
            currNode = queue.popleft()

            # Reverse order of current node values if going from right to left
            if leftRight:
                currLevel.append(currNode.val)
            else:
                currLevel.appendleft(currNode.val)

            if currNode.left is not None:
                nextQueue.append(currNode.left)
            if currNode.right is not None:
                nextQueue.append(currNode.right)

            # When end of level is reached
            if len(queue) == 0:
                zigzagNodes.append(currLevel)

                # Switch queue to next level queue, and reset variables
                queue = deque(nextQueue)
                nextQueue = []
                currLevel = deque([])

                # Flip boolean flag for next level
                leftRight = not leftRight

        return zigzagNodes

    def __init__(self):
        self.levelVals = {}

    def dfs(self, node, level=0):
        if node is None:
            return

        if level not in self.levelVals:
            self.levelVals[level] = deque([])

        if level % 2 == 0:
            self.levelVals[level].append(node.val)
        else:
            self.levelVals[level].appendleft(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)

    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []

        self.dfs(root)

        zigzagLevels = []
        for i in range(len(self.levelVals.keys())):
            zigzagLevels.append(self.levelVals[i])

        return zigzagLevels
