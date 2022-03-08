"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        递归
        :param root:
        :return:
        """
        if not root:
            return 0

        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth(root.children[i]))
        return depth + 1

    def maxDepth_2(self, root: 'Node') -> int:
        """
        递归
        :param root:
        :return:
        """
        if not root:
            return 0

        dq = deque([root])
        node = root
        num = 0
        while dq:
            n = len(dq)
            num += 1
            for _ in range(n):
                node = dq.popleft()
                if node.children:
                    dq.extend(node.children)
        return num
