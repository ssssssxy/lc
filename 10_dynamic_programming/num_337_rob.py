# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_tree(cur):
            if not cur:
                return [0, 0]  # 下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。

            left_val = rob_tree(cur.left)
            right_val = rob_tree(cur.right)

            # 偷cur
            val1 = cur.val + left_val[0] + right_val[0]
            # 不偷cur
            val2 = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])

            return [val2, val1]

        val = rob_tree(root)
        return max(val[0], val[1])

    # def rob(self, root: TreeNode) -> int:
    #     result = self.rob_tree(root)
    #     return max(result[0], result[1])

    # def rob_tree(self, node):
    #     if node is None:
    #         return (0, 0) # (偷当前节点金额，不偷当前节点金额)
    #     left = self.rob_tree(node.left)
    #     right = self.rob_tree(node.right)
    #     val1 = node.val + left[1] + right[1] # 偷当前节点，不能偷子节点
    #     val2 = max(left[0], left[1]) + max(right[0], right[1]) # 不偷当前节点，可偷可不偷子节点
    #     return (val1, val2)

