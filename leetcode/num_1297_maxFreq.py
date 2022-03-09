import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # results = {}
        # left = 0
        # right = minSize
        # while right <= len(s):
        #     if len(set(s[left:right])) <= maxLetters and (right - left)<=maxSize and (right - left)>=minSize:
        #         results[s[left:right]] = results[s[left:right]] + 1 if results.get(s[left:right]) else 1
        #         right += 1
        #     elif len(set(s[left: right])) <= maxLetters and (right - left) > maxSize:
        #         left += 1
        #     elif len(set(s[left:right])) <= maxLetters and (right - left) < minSize:
        #         right += 1
        #     elif len(set(s[left:right])) > maxLetters and (right - left)<=maxSize and (right - left)>=minSize:
        #         left += 1
        #     elif len(set(s[left:right])) > maxLetters and (right - left) > maxSize:
        #         left += 1
        #     elif len(set(s[left: right])) > maxLetters and (right - left) < minSize:
        #         right += 1
        # return max(results.values())

        n = len(s)
        d = collections.defaultdict(int)
        for i in range(n - minSize + 1):
            temp = s[i:i + minSize]
            c = set(temp)
            if len(c) <= maxLetters:
                d[temp] += 1
        return max(d.values()) if d else 0

s = Solution()
s.maxFreq(s="aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3)