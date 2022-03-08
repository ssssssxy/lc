class Solution:
    def replaceSpace(self, s: str) -> str:
        list_s = list(s)
        k_n = s.count(" ")
        len_s = len(s)
        list_s.extend([" "] * k_n * 2)
        len_new_s = len(list_s)

        left = len_s - 1
        right = len_new_s - 1

        while left >= 0:
            if list_s[left] != " ":
                list_s[right] = list_s[left]
                left -= 1
                right -= 1
            else:
                list_s[right] = "0"
                list_s[right - 1] = "2"
                list_s[right - 2] = "%"
                right = right - 3
                left -= 1

        return "".join(list_s)

        # res = []
        # for c in s:
        #     if c == ' ': res.append("%20")
        #     else: res.append(c)
        # return "".join(res)
        #  8.46%  46%




