class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_len = len(res)
        for i in s:
            if i in res:
                index_ = res.index(i)
                res = res[index_+1:]

            res.append(i)
            max_len = max(max_len, len(res))
        return max_len



        # 哈希集合，记录每个字符是否出现过
        # occ = set()
        # n = len(s)
        # # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        # rk, ans = -1, 0
        # for i in range(n):
        #     if i != 0:
        #         # 左指针向右移动一格，移除一个字符
        #         occ.remove(s[i - 1])
        #     while rk + 1 < n and s[rk + 1] not in occ:
        #         # 不断地移动右指针
        #         occ.add(s[rk + 1])
        #         rk += 1
        #     # 第 i 到 rk 个字符是一个极长的无重复字符子串
        #     ans = max(ans, rk - i + 1)
        # return ans


        # hashtable = {}
        # l, maxLenth = -1, 0
        # for i in range(len(s)):
        #     if s[i] in hashtable:
        #         l = max(l, hashtable[s[i]])
        #     hashtable[s[i]] = i
        #     maxLenth = max(maxLenth, i - l)
        # return maxLenth


s = Solution()
s.lengthOfLongestSubstring(s="abbc")