# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)
        in_left_order = inorder[0:root_index]
        in_right_order = inorder[root_index + 1:]
        pre_left_order = preorder[1:len(in_left_order) + 1]
        pre_right_order = preorder[len(in_left_order) + 1:]
        root.left = self.buildTree(pre_left_order, in_left_order)
        root.right = self.buildTree(pre_right_order, in_right_order)
        return root

        # def build(pre, ino):
        #     if len(pre) == 0:
        #         return
        #     elif len(pre) == 1:
        #         return TreeNode(pre[0])

        #     root_val = pre[0]
        #     root = TreeNode(root_val)

        #     root_index = ino.index(root_val)
        #     in_left_order = ino[0:root_index]
        #     in_right_order = ino[root_index + 1:]
        #     pre_left_order = pre[1:len(in_left_order) + 1]
        #     pre_right_order = pre[len(in_left_order)+1:]
        #     root.left = build(pre_left_order, in_left_order)
        #     root.right = build(pre_right_order, in_right_order)
        #     return root

        # root = build(preorder, inorder)
        # return root
