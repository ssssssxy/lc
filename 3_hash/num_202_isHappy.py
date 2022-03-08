class Solution:
    def isHappy(self, n: int) -> bool:
        def get_result(num):
            result = 0
            while num != 0:
                num, rem = divmod(num, 10)
                result = result + rem ** 2
            return result

        sum_result = get_result(n)
        mid_result = set()

        while sum_result not in mid_result and sum_result != 1:
            mid_result.add(sum_result)
            sum_result = get_result(sum_result)

        return sum_result == 1


