# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def build(ino, post):
            if len(post) == 1:
                return TreeNode(post[-1])
            if len(post) == 0:
                return
            root_val = post[-1]
            root = TreeNode(root_val)
            root_index = ino.index(root_val)
            in_left_tree = ino[0:root_index]
            in_right_tree = ino[root_index+1:]
            post_left_tree = post[0:len(in_left_tree)]
            post_right_tree = post[len(in_left_tree): -1]
            root.left = build(in_left_tree, post_left_tree)
            root.right = build(in_right_tree, post_right_tree)
            return root

        root = build(inorder, postorder)
        return root


