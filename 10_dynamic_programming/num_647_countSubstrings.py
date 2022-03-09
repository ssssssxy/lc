class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态阈值
        # dp = [[0] * len(s) for _ in range(len(s))]

        # res = 0
        # for i in range(len(s)-1, -1, -1):
        #     for j in range(i, len(s)):
        #         if s[i] == s[j]:
        #             if j-i <= 1:
        #                 res += 1
        #                 dp[i][j] = 1
        #             elif dp[i+1][j-1]:
        #                 res += 1
        #                 dp[i][j] = 1
        # return res

        # 双指针
        def extend_s(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res

        n = len(s)
        results = 0
        for i in range(len(s)):
            res1 = extend_s(i, i)
            res2 = extend_s(i, i + 1)
            results = results + res1 + res2
        return results