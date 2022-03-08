class Solution:
    def __init__(self):
        self.results = []
        self.result = []

    def is_palindrome(self, s, start, end):
        left = start
        right = end
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtracking(self, s, start_index):

        if start_index >= len(s):
            self.results.append(self.result[:])
            return

        for i in range(start_index, len(s)):
            if self.is_palindrome(s, start_index, i):
                self.result.append(s[start_index:i + 1])
                self.backtracking(s, i + 1)
                self.result.pop()
            else:
                continue

    def partition(self, s: str):
        self.backtracking(s, 0)
        return self.results


s = Solution()
print(s.partition("aaabbb"))