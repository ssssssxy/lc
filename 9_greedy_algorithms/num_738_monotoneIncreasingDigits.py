class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s_n = list(str(n))
        for i in range(len(s_n)-1, 0, -1):
            if int(s_n[i]) < int(s_n[i-1]):
                s_n[i:] = "9" * (len(s_n) - i)
                s_n[i-1] = str(int(s_n[i-1])-1)
        return int("".join(s_n))