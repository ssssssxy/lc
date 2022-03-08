class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        # 贪心算法
        # min_price = prices[0]
        # res = 0
        # for i in range(1, len(prices)):
        # // 情况二：相当于买入
        #     if prices[i] < min_price:
        #         min_price = prices[i]

        # // 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
        #     elif prices[i] >= min_price  and prices[i] < min_price + fee:
        #         continue

        # // 计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
        #     else:
        #         res += prices[i] - min_price - fee
        #         min_price = prices[i] - fee  // 情况一，这一步很关键
        # return res

        # 动态规划
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
        return dp[-1][-1]

