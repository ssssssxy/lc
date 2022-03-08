class Solution:
    def maxSubArray(self, nums) -> int:
        # 贪心
        # max_sum = -float("inf")
        # sum_ = 0
        # for i in nums:
        #     sum_ += i
        #     if sum_ > max_sum:
        #         max_sum = sum_
        #     if sum_ <= 0:
        #         sum_ = 0

        # return max_sum

        # 动态规划
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
