class Solution:
    def __init__(self):
        self.results = []
        self.result = []
        self.sum_ = 0

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        def backtracking(start_index):
            if self.sum_ > target:
                return
            elif self.sum_ == target:
                self.results.append(self.result[:])
                return
            for i in range(start_index, len(candidates)):
                if self.sum_ + candidates[i] > target:
                    return
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                self.sum_ += candidates[i]
                self.result.append(candidates[i])
                backtracking(i+1)
                self.sum_ -= candidates[i]
                self.result.pop()
        backtracking(0)
        return self.results

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5,5], 11))