class Solution:
    def maxProfit(self, prices) -> int:
        # result = 0
        # for i in range(len(prices) - 1):
        #     if prices[i+1] - prices[i] > 0:
        #         result += prices[i+1] - prices[i]
        # return result

        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        return dp[-1][1]
