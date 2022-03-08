class Solution:
    def __init__(self):
        self.results = []
        self.result = []

    def backtracking(self, s, start_index):
        if len(self.result) > 4:
            return
        if start_index == len(s):
            self.results.append(".".join(self.result))
            return

        for i in range(start_index, len(s)):
            if len(self.result) == 3 and (len(s) - start_index) > 3:
                break
            if len(self.result) == 3 and (len(s) - start_index) <= 3 and (len(s) - start_index) >1 and s[start_index] == '0':
                break
            if (len(s[start_index: i+1]) > 1 and s[start_index] == '0') or int(s[start_index: i+1]) > 255:
                break
            self.result.append(s[start_index: i + 1])
            self.backtracking(s, i+1)
            self.result.pop()

    def restoreIpAddresses(self, s: str):
        if len(s) < 4 or len(s) > 12:
            return []
        self.backtracking(s, 0)
        return self.results


s = Solution()
# print(s.restoreIpAddresses("101523123"))
print(s.restoreIpAddresses("0000"))
