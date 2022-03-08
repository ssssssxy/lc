class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:
                res += 1
        return res