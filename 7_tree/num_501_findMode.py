# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode):
        pre = None
        cur = root
        stack = []
        max_count = 0
        count = 0
        results = []
        while cur or stack:

            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1

                if count == max_count:
                    results.append(cur.val)
                if count > max_count:
                    max_count = count
                    results.clear()
                    results.append(cur.val)
                pre = cur
                cur = cur.right
        return results

