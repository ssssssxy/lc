# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        left = 0
        right = len(nums) - 1

        def _sortedArrayToBST(nums, left, right):
            if left > right:
                return None

            root_index = left + (right - left) // 2
            root = TreeNode(nums[root_index])
            root.left = _sortedArrayToBST(nums, left, root_index - 1)
            root.right = _sortedArrayToBST(nums, root_index + 1, right)
            return root

        root = _sortedArrayToBST(nums, left, right)
        return root



