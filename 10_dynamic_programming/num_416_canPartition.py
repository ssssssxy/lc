class Solution:
    def canPartition(self, nums) -> bool:
        target, redis = sum(nums) // 2, sum(nums) % 2
        if redis != 0:
            return False
        dp = [0] * (target + 1)

        for i in range(1, len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return dp[-1] == target



s = Solution()
s.canPartition([1,5,11,5])