# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        dq = deque([root])
        num = 0
        while dq:
            n = len(dq)
            num += 1
            for _ in range(n):
                root = dq.popleft()
                if not root.left and not root.right:
                    return num
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
        return num

    def minDepth_2(self, root) -> int:
        """
        递归
        :param root:
        :return:
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10 ** 9

        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1


