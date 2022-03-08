# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def judge(node1, node2):
            if node1 and not node2:
                return False
            elif not node1 and node2:
                return False
            elif not node1 and not node2:
                return True
            elif node1 and node2 and node1.val != node2.val:
                return False

            res1 = judge(node1.left, node2.right)
            res2 = judge(node1.right, node2.left)
            if res1 and res2:
                return True
            else:
                return False

        return judge(root.left, root.right)

