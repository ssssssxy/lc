# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def pathSum(self, root, targetSum: int):
        if not root:
            return []
        results = []
        stack = [root]
        paths = [[root.val]]
        while stack:
            node = stack.pop()
            path1 = copy.deepcopy(paths.pop())
            path2 = copy.deepcopy(path1)

            if not node.left and not node.right and sum(path1) == targetSum:
                results.append(path1)

            if node.left:
                stack.append(node.left)
                path1.append(node.left.val)
                paths.append(path1)
            if node.right:
                stack.append(node.right)
                path2.append(node.right.val)
                paths.append(path2)

        return results