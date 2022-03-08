# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:

        def get_depth(root):

            if not root:
                return 0

            if (left_depth := get_depth(root.left)) == -1:
                return -1
            if (right_depth := get_depth(root.right)) == -1:
                return -1
            if abs(left_depth - right_depth) > 1:
                return -1
            else:
                return 1 + max(left_depth, right_depth)

        res = get_depth(root)
        if res == -1:
            return False
        else:
            return True
