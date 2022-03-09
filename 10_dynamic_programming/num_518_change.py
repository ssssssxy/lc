class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j-coins[i]]
        return dp[-1]

s = Solution()
print(s.change(5, [1,2,5]))