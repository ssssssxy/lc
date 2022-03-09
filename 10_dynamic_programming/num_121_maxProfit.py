class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        # dp[i][0] 表示第i天持有股票所得最多现金 , dp[i][1] 表示第i天不持有股票所得最多现金
        for i in range(1, len(prices)):
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])

        return max(dp[-1][0], dp[-1][1])

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))