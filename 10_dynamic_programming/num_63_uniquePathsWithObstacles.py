class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        row_obstacle = obstacleGrid[0].index(1) if 1 in obstacleGrid[0] else -1
        if row_obstacle != -1:
            for i in range(row_obstacle, n):
                dp[0][i] = 0

        column_obstacle = -1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                column_obstacle = i
                break
        if column_obstacle != -1:
            for i in range(column_obstacle, m):
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(dp)
        return dp[-1][-1]

    def uniquePathsWithObstacles_2(self, obstacleGrid) -> int:
        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,1]]))
print(s.uniquePathsWithObstacles([[0,1], [1,0]]))
s.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print(s.uniquePathsWithObstacles([[1,0]]))