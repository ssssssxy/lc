# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def findBottomLeftValue(self, root) -> int:
        dq = deque([root])
        while dq:
            n = len(dq)
            for i in range(n):
                if i == 0:
                    results = dq[0].val
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return results
