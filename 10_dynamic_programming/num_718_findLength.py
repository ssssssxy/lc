class Solution:
    def findLength(self, nums1, nums2) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]

        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
        return res