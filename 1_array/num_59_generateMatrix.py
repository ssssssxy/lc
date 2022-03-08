class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left = 0
        right = n - 1
        up = 0
        down = n - 1
        number = 1
        while left < right and up < down:
            # 从左到右
            for i in range(left, right):
                matrix[up][i] = number
                number += 1

            # 从上倒下
            for i in range(up, down):
                matrix[i][right] = number
                number += 1

            # 从右到左
            for i in range(right, left, -1):
                matrix[down][i] = number
                number += 1

            # 从下到上
            for i in range(down, up, -1):
                matrix[i][left] = number
                number += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        if n % 2 != 0:
            matrix[(n - 1) // 2][(n - 1) // 2] = n * n

        return matrix

