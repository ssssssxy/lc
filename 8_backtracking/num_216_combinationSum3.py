class Solution:
    def combinationSum3(self, k: int, n: int):
        results = []
        path = []
        sum_ = 0
        def backtracking(n, k, start_index):
            nonlocal sum_
            if sum(path) > n:
                return
            if len(path) == k and sum(path) == n:
                results.append(path[:])
                return
            for i in range(start_index, 10 - (k - len(path))+1):
                path.append(i)
                sum_ += i
                backtracking(n, k, i + 1)
                sum_ -= 1
                path.pop()
        backtracking(n, k, 1)
        return results

s = Solution()
s.combinationSum3(3, 7)