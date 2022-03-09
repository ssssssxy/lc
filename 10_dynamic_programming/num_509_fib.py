class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        a = 0
        b = 1
        c = 0
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c

