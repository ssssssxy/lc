# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        value = root.val
        if value == val:
            return root
        elif value > val:
            return self.searchBST(root.left, val)
        elif value < val:
            return self.searchBST(root.right, val)