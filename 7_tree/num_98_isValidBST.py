# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max = -float("INF")
        def __isValidBST(node):
            nonlocal cur_max

            if not node:
                return True

            res1 = __isValidBST(node.left)
            if cur_max < node.val:
                cur_max = node.val
            else:
                return False
            res2 = __isValidBST(node.right)
            return res1 and res2

        return __isValidBST(root)
