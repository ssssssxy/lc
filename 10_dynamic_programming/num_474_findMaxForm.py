class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str_ in strs:
            zeros_ = str_.count("0")
            ones_ = str_.count("1")
            for i in range(m, zeros_ - 1, -1):
                for j in range(n, ones_ - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros_][j - ones_] + 1)
        return dp[-1][-1]


s = Solution()
s.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3)