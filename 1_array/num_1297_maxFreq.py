class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize or not maxLetters:
            return 0
        hashmap = {}
        i = 0
        j = 1
        while j <= len(s):
            letters = len(set(s[i:j]))
            if letters <= maxLetters and len(s[i:j]) < minSize:
                j += 1
            elif letters > maxLetters and len(s[i:j]) <= maxSize:
                if j < len(s):
                    i += 1
                    j += 1
                else:
                    i += 1
            elif len(s[i:j]) >= minSize and len(s[i:j]) <= maxSize and letters <= maxLetters:
                hashmap[s[i:j]] = hashmap[s[i:j]] + 1 if s[i:j] in hashmap else 1
                if j < len(s):
                    j += 1
                else:
                    i += 1

            elif len(s[i:j]) > maxSize:
                i += 1
            if len(s) - i < minSize:
                break
        return max(hashmap.values())


s = Solution()
# print(s.maxFreq("aaaa", 1, 3, 3))
# print(s.maxFreq("aababcaab", 2, 3, 4))
print(s.maxFreq("aabcabcab", 2, 2, 3))
