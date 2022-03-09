class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        # dp = [0] * (target + 1)
        # dp[0] = 1
        # for i in range(0, len(nums)):
        #     for j in range(1, target+1):
        #         dp[j] = 0
        #         for k in range(i+1):
        #             if j-nums[k] >= 0:
        #                 dp[j] += dp[j-nums[k]]
        # return dp[-1]


        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[-1]


s = Solution()
print(s.combinationSum4(nums=[1,2,3], target=4))

