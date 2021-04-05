from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        valueQueue = deque(preorder)
        root = TreeNode(valueQueue.popleft())
        nodeStack = [root]

        while len(valueQueue) > 0:
            currVal = valueQueue[0]
            nextNode = nodeStack[-1]

            if currVal < nextNode.val:
                nextNode.left = TreeNode(valueQueue.popleft())
                nodeStack.append(nextNode.left)
            else:
                nextNode = nodeStack.pop()
                if len(nodeStack) == 0 or currVal < nodeStack[-1].val:
                    nextNode.right = TreeNode(valueQueue.popleft())
                    nodeStack.append(nextNode.right)

        return root
