# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        results = []

        def post_order(root):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            results.append(root.val)

        post_order(root)
        return results

    def postorderTraversal_2(self, root):
        results = []
        if not root:
            return results
        node = root
        stack = []
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if not node.right or node.right == prev:
                results.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return results

    def postorderTraversal_3(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]
