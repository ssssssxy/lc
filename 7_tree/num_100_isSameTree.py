# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        def judge(node1, node2):
            if node1 and not node2:
                return False
            elif not node1 and node2:
                return False
            elif node1 and node2 and node1.val != node2.val:
                return False
            elif not node1 and not node2:
                return True

            res1 = judge(node1.left, node2.left)
            res2 = judge(node1.right, node2.right)
            if res1 and res2:
                return True
            else:
                return False

        res = judge(p, q)
        return res