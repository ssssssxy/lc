class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                b = int(tmp.pop())
                a = int(tmp.pop())
                if i == "+":
                    tmp.append(a + b)
                elif i == "-":
                    tmp.append(a - b)
                elif i == "*":
                    tmp.append(a * b)
                elif i == "/":
                    tmp.append(int(a/b))
            else:
                tmp.append(i)
        return int(tmp[0])
