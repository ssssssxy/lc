"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root):
        if not root:
            return root

        stack = [root]
        results = []
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.children:
                stack.extend(node.children)
        return results[::-1]