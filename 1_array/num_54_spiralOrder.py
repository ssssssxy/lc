class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n - 1
        up = 0
        down = m - 1
        ans = []

        while left < right and up < down:
            for i in range(left, right):
                ans.append(matrix[up][i])

            for i in range(up, down):
                ans.append(matrix[i][right])

            for i in range(right, left, -1):
                ans.append(matrix[down][i])

            for i in range(down, up, -1):
                ans.append(matrix[i][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        if left == right:
            for i in range(up, down + 1):
                ans.append(matrix[i][left])

        if up == down and left != right:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])

        return ans

