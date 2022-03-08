# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()

    def convertBST(self, root):
        node = root
        if not node:
            return None

        def convert(node):
            if not node:
                return None

            convert(node.right)
            node.val = self.pre.val + node.val
            self.pre = node
            convert(node.left)

        convert(node)
        return root


