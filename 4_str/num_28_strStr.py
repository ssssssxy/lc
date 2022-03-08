class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        left = right = 0
        while right < len(haystack) and left < len(needle):
            if haystack[right] == needle[left]:
                if left == 0:
                    cur = right
                right += 1
                left += 1
            else:
                right += 1
                left = 0

        if left == len(needle):
            return cur
        else:
            return -1

s = Solution()
s.strStr("mississippi", "issip")

