class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # dp = [0] * len(cost)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, len(cost)):
        #     dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # return min(dp[-1], dp[-2])
        a = cost[0]
        b = cost[1]
        c = 0
        for i in range(2, len(cost)):
            c = min(a, b) + cost[i]
            a = b
            b = c
        return min(a, b)

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
import copy
a = [1]
a.copy()