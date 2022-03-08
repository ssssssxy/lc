class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left #中
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root