class Solution:
    def combine(self, n: int, k: int):
        results = []
        result = []

        def backtracking(n, k, start_index):
            if len(result) == k:
                results.append(result[:])
                return
            for i in range(start_index,  n - (k - len(result)) + 2):
                result.append(i)
                backtracking(n, k, i + 1)
                result.pop()

        backtracking(n, k, 1)
        return results

s = Solution()
s.combine(4, 2)