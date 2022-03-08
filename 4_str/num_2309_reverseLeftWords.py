class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_list = list(s)

        def reverse(left, right):
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(n, len(s_list) - 1)
        reverse(0, len(s_list) - 1)

        return ('').join(s_list)