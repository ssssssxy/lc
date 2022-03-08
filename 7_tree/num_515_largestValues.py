# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root):
        results = []
        if not root:
            return results

        dq = deque([root])
        while dq:
            n = len(dq)
            max_ = float('-inf')
            for _ in range(n):
                root = dq.popleft()
                max_ = max(root.val, max_)
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            results.append(max_)
        return results