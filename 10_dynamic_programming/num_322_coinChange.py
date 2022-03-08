class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # 错误的
        # coins.sort()
        # dp = [-1] * (amount + 1)
        # dp[0] = 0

        # for i in range(len(coins)):
        #     for j in range(1, amount + 1):
        #         a, b = j // coins[i], j % coins[i]
        #         for k in range(a, 0, -1):
        #             m = j - coins[i] * k
        #             if dp[m] == -1:
        #                 continue
        #             dp[j] = k + dp[m]
        #             break

        # return dp[-1]

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[-1] if dp[-1] < amount + 1 else -1


s = Solution()
print(s.coinChange([186,419,83,408] ,6249))