# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root is None or p is None:
            return None

        if p.right is not None:
            currNode = p.right
            while currNode.left is not None:
                currNode = currNode.left
            return currNode

        currNode = root
        successor = None
        while currNode is not None:
            if currNode.val == p.val:
                return successor

            elif p.val < currNode.val:
                successor = currNode
                currNode = currNode.left
            else:
                currNode = currNode.right

        return successor
