# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)  # 右

        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val

        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum  # 中