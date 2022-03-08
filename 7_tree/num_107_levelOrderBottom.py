# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        results = []
        if not root:
            return results

        dq = deque([root])
        while dq:
            n = len(dq)
            result = []
            for _ in range(n):
                root = dq.popleft()
                result.append(root.val)
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            results.append(result)

        results.reverse()
        return results