# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        min_diff = float("inf")

        def __getMinimumDifference(root):
            if not root:
                return None

            if root.left:
                __getMinimumDifference(root.left)
            res.append(root.val)
            if root.right:
                __getMinimumDifference(root.right)
            return res

        __getMinimumDifference(root)
        for i in range(len(res) - 1):
            min_diff = min(min_diff, abs(res[i + 1] - res[i]))
        return min_diff



