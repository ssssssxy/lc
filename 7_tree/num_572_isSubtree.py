# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
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

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        res = judge(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return res

    # def isSubtree(self, s, t):
    #     """
    #     :type s: TreeNode
    #     :type t: TreeNode
    #     :rtype: bool
    #     """
    #     if not s and not t:
    #         return True
    #     if not s or not t:
    #         return False
    #     return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # def isSameTree(self, s, t):
    #     if not s and not t:
    #         return True
    #     if not s or not t:
    #         return False
    #     return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

