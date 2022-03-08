# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        """
        递归
        :param root:
        :return:
        """
        results = []

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            results.append(root.val)
            in_order(root.right)

        in_order(root)
        return results

    def inorderTraversal_2(self, root):
        """
        迭代
        :param root:
        :return:
        """
        results = []
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            results.append(node.val)
            node = node.right
        return results