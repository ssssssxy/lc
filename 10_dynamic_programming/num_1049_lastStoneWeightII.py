class Solution:
    def lastStoneWeightII(self, stones) -> int:

        target = sum(stones) // 2

        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones) - 2 * dp[-1]


s = Solution()
print(s.lastStoneWeightII([31,26,33,21,40]))