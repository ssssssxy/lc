class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for i in range(2 * k + 1):
            if i % 2 != 0:
                dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(2 * k + 1):
                if j == 0:
                    dp[i][0] = dp[i - 1][0]
                elif j % 2 == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        return dp[-1][-1]
