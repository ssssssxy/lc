class Solution:
    def reverseWords(self, s: str) -> str:
        # list_s = list(s)
        # left = right = 0
        # n = len(list_s)
        # while right < n - 1:
        #     while right != n-1 and list_s[right + 1] != " ":
        #         right += 1
        #     tmp = right
        #     while left < right:
        #         list_s[left], list_s[right] = list_s[right], list_s[left]
        #         left += 1
        #         right -= 1
        #     left = right = tmp + 2
        # return "".join(list_s)

        list_s = list(s)
        left = right = len(list_s) - 1
        new_s = []
        while right >= 0:
            while right >= 0 and list_s[right] == " ":
                left = right = right - 1
            while right > 0 and list_s[right - 1] != " ":
                right -= 1
            if right >= 0:
                new_s.extend(list_s[right: left+1])
                new_s.append(" ")
                left = right = right - 2
        return "".join(new_s)[:-1]

s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("a  hello world  "))