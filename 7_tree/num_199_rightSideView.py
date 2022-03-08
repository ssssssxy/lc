# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root):
        results = []
        if not root:
            return results
        dq = deque([root])

        while dq:
            n = len(dq)
            results.append(dq[-1].val)

            for i in range(n):
                root = dq.popleft()
                # if i == n - 1:
                #     results.append(root.val)

                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
        return results

