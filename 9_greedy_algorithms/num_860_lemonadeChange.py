class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        res = {}
        for i in bills:
            if i == 5:
                res[5] = res.get(5, 0) + 1
            elif i == 10:
                res[10] = res.get(10, 0) + 1
                res[5] = res.get(5, 0) - 1
                if res[5] < 0:
                    return False
            elif i == 20:
                if res.get(10, 0) >= 1 and res.get(5, 0) >= 1:
                    res[10] = res.get(10, 0) - 1
                    res[5] = res.get(5, 0) - 1
                else:
                    res[5] = res.get(5, 0) - 3
                if res.get(5, 0) < 0 or res.get(10, 0) < 0:
                    return False

        return True

