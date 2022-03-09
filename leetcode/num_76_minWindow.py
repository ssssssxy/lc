class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = {}
        need_count = 0
        for i in t:
            need_dict[i] = need_dict.get(i, 0) + 1
            need_count += 1

        left = right = 0
        res_len = float("inf")
        res = ""
        for right in range(len(s)):
            if s[right] in need_dict:
                if need_count > 0 and need_dict[s[right]] > 0:
                    need_count -= 1
                need_dict[s[right]] -= 1

            while not need_count:
                if s[left] in need_dict:
                    if need_dict.get(s[left]) < 0:
                        need_dict[s[left]] += 1
                        left += 1
                    else:
                        if res_len > len(s[left:right + 1]):
                            res_len = len(s[left:right + 1])
                            res = s[left:right + 1]
                        break
                else:
                    left += 1
        return res

s = Solution()
s.minWindow("bba", "ab")



