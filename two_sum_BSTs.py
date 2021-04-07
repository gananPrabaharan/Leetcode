from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if root1 is None or root2 is None:
            return False

        firstTreeSet = set()

        # Traverse through tree/root 1, and add values to a set O(n) time, O(n) space
        nodeQueue = deque([root1])
        while len(nodeQueue) > 0:
            currNode = nodeQueue.popleft()
            firstTreeSet.add(currNode.val)
            if currNode.left is not None:
                nodeQueue.append(currNode.left)
            if currNode.right is not None:
                nodeQueue.append(currNode.right)

        # Traverse through tree 2, and check if target-currNode.val is in tree 1 set O(n) time
        nodeQueue = deque([root2])
        while len(nodeQueue) > 0:
            currNode = nodeQueue.popleft()
            if target - currNode.val in firstTreeSet:
                return True
            if currNode.left is not None:
                nodeQueue.append(currNode.left)
            if currNode.right is not None:
                nodeQueue.append(currNode.right)

        return False