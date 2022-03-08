class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i == "(":
                tmp.append(")")
            elif i == "{":
                tmp.append("}")
            elif i == "[":
                tmp.append("]")
            else:
                if not tmp:
                    return False
                j = tmp.pop()
                if i != j:
                    return False
        if tmp:
            return False
        else:
            return True


