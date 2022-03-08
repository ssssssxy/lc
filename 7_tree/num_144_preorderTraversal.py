# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        """
        迭代
        :param root:
        :return:
        """
        results = []

        def pre_order(root):
            if not root:
                return
            results.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return results

    def preorderTraversal_2(self, root):
        """
        迭代
        :param root:
        :return:
        """
        results = []
        if not root:
            return results
        node = root
        stack = []
        while stack or node:
            while node:
                results.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return results

    def preorderTraversal_3(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result