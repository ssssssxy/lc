# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        dq = deque([root])
        num = 0
        while dq:
            num += 1
            n = len(dq)
            for _ in range(n):
                root = dq.popleft()
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
        return num

    def maxDepth_2(self, root) -> int:
        """
        递归
        :param root:
        :return:
        """
        if not root:
            return 0

        def get_max(node):
            if not node:
                return 0

            left_num = get_max(node.left)
            right_num = get_max(node.right)
            num = 1 + max(left_num, right_num)
            return num
        num = get_max(root)
        return num