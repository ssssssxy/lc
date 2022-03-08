# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None
        max_value = max(nums)
        max_index = nums.index(max_value)
        root = TreeNode(max_value)
        left_tree = nums[0:max_index]
        right_tree = nums[max_index+1:]
        root.left = self.constructMaximumBinaryTree(left_tree)
        root.right = self.constructMaximumBinaryTree(right_tree)
        return root