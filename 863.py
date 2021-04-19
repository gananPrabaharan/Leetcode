from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.parentMap = {}
        self.targetParents = set()
        self.k = None
        self.target = None
        self.resultNodes = []

    def setParentMap(self, root):
        nodeStack = [root]
        self.parentMap = {root: None}
        while len(nodeStack) > 0:
            node = nodeStack.pop()

            if node.left is not None:
                nodeStack.append(node.left)
                self.parentMap[node.left] = node

            if node.right is not None:
                nodeStack.append(node.right)
                self.parentMap[node.right] = node

        parent = self.target
        while parent is not None:
            self.targetParents.add(parent)
            parent = self.parentMap[parent]

    def getDistance(self, node, distance):
        if node in self.targetParents:
            return distance - 1
        else:
            return distance + 1

    def traverse(self):
        topNode = self.target
        distance = 0
        while distance < self.k:
            if self.parentMap[topNode] is None:
                break

            topNode = self.parentMap[topNode]
            distance += 1

        nodeQueue = deque([(topNode, distance)])

        while len(nodeQueue) > 0:
            currNode, currDistance = nodeQueue.popleft()
            if currDistance > self.k:
                continue

            if currDistance == self.k:
                self.resultNodes.append(currNode.val)

            if currNode.left is not None:
                newDistance = self.getDistance(currNode.left, currDistance)
                nodeQueue.append((currNode.left, newDistance))
            if currNode.right is not None:
                newDistance = self.getDistance(currNode.right, currDistance)
                nodeQueue.append((currNode.right, newDistance))

    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        if K == 0:
            return [target.val]

        self.k = K
        self.target = target
        self.setParentMap(root)
        self.traverse()

        return self.resultNodes
