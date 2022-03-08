# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        results = []
        stack = [root]
        path_st = [str(root.val)]

        while stack:
            path = path_st.pop()
            node = stack.pop()
            if not node.left and not node.right:
                results.append(path)

            if node.left:
                stack.append(node.left)
                path_st.append(path + "->" + str(node.left.val))

            if node.right:
                stack.append(node.right)
                path_st.append(path + "->" + str(node.right.val))

        return results