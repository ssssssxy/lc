class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp)

s = Solution()
s.findLengthOfLCIS([1,3,5,4,7])