"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root):
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
                if root.children:
                    dq.extend(root.children)
            results.append(result)

        return results

