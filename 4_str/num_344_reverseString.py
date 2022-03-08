class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            a = s[left]
            s[left] = s[right]
            s[right] = a
            left += 1
            right -= 1