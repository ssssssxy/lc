class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        num = len(list_s) - 1
        i = 0
        while 2*k*i <= num:
            left = 2*k*i
            right = 2*k*i - 1 + k
            if right > num:
                right = num
            while left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
            i += 1
        return "".join(list_s)