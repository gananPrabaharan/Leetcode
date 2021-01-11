# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cumulative_sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node is None:
                return

            if low <= node.val <= high:
                self.cumulative_sum += node.val

            if node.val < high:
                dfs(node.right)

            if node.val > low:
                dfs(node.left)

        dfs(root)
        return self.cumulative_sum
