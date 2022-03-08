# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root):
        results = []
        if not root:
            return results

        dq = deque([root])
        while dq:
            n = len(dq)
            sum_ = 0
            for _ in range(n):
                root = dq.popleft()
                sum_ += root.val
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            results.append(sum_ / n)
        return results