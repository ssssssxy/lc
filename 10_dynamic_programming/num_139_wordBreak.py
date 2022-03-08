class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[0] = True
        # for word in wordDict:
        for i in range(1, len_s + 1):

            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i - len(word)] and word == s[i - len(word):i])
        return dp[-1]

s = Solution()
# print(s.wordBreak("leetcode", ["leet","code"]))
print(s.wordBreak("applepenapple", ["apple","pen"]))