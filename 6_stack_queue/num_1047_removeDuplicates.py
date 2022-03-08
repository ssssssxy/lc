class Solution:
    def removeDuplicates(self, s: str) -> str:
        tmp = []
        for i in s:
            if tmp and tmp[-1] == i:
                tmp.pop()
            else:
                tmp.append(i)
        return "".join(tmp)