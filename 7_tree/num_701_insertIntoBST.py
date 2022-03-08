# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        flag = None
        pre = None
        while node:
            pre = node
            if node.val > val:
                node = node.left
                flag = "left"
            elif node.val < val:
                node = node.right
                flag = "right"
        if flag == "left":
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root

