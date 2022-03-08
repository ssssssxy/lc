class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        if not nums1 or not nums2:
            return 0
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]