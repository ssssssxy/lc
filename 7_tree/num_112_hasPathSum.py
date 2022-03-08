# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        stack = [root]
        sum_ = [root.val]
        while stack:
            node = stack.pop()
            part_sum = sum_.pop()
            if not node.left and not node.right and part_sum == targetSum:
                return True

            if node.left:
                stack.append(node.left)
                sum_.append(part_sum + node.left.val)
            if node.right:
                stack.append(node.right)
                sum_.append(part_sum + node.right.val)
        return False

