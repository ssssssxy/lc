class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                # else:
                #     dp[i] = max(dp[i], dp[j])
        return dp[-1]

    # Dynamic programming + Dichotomy.
    def lengthOfLIS_2(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res


s = Solution()
# s.lengthOfLIS([4,10,4,3,8,9])
print(s.lengthOfLIS_2([9,10,2,11,7,101,18]))