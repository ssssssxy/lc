class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftHeight = 0 #这里初始为0是有目的的，为了下面求指数方便
        rightHeight = 0
        while left: #求左子树深度
            left = left.left
            leftHeight += 1
        while right: #求右子树深度
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return (2 << leftHeight) - 1 #注意(2<<1) 相当于2^2，所以leftHeight初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1