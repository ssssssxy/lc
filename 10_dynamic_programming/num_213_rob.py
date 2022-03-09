class Solution:
    def rob(self, nums) -> int:
        # 有1号
        dp1 = [0] * (len(nums))
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])

        # 没有1号
        dp2 = [0] * (len(nums))
        dp2[1] = nums[1]
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        return max(dp1[-2], dp2[-1])

s = Solution()
print(s.rob([2,3,2]))