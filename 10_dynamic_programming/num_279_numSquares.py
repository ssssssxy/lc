import math

class Solution:
    def numSquares(self, n: int) -> int:
        m = math.floor(pow(n, 0.5))
        nums = []
        for i in range(1, m + 1):
            nums.append(i * i)

        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for num in nums:
            for i in range(num, n + 1):
                dp[i] = min(dp[i], dp[i - num] + 1)

        return dp[-1]