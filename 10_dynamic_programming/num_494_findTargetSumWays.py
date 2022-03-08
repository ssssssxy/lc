class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        sum_ = sum(nums)
        if abs(sum_) < target or (target + sum_) % 2 != 0:
            return 0
        x = (target + sum_) // 2
        dp = [0] * (x + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(x, nums[i] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]
        return dp[-1]

s = Solution()
print(s.findTargetSumWays())
print(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3))

