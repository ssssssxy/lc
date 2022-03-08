class Solution:
    def __init__(self):
        self.results = []
        self.result = []
        self.sum_ = 0

    def combinationSum(self, candidates, target: int):
        candidates.sort()
        def backtracking(start_index):
            if self.sum_ > target:
                return
            elif self.sum_ == target:
                self.results.append(self.result[:])
            for i in range(start_index, len(candidates)):
                if self.sum_ + candidates[i] > target:
                    return
                self.sum_ += candidates[i]
                self.result.append(candidates[i])
                backtracking(i)
                self.result.pop()
                self.sum_ -= candidates[i]
        backtracking(0)
        return self.results
