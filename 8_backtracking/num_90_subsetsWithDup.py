class Solution:
    def __init__(self):
        self.results = []
        self.result = []

    def subsetsWithDup(self, nums):

        def backtracking(nums, start_index):
            self.results.append(self.result[:])
            if start_index == len(nums):
                return
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                self.result.append(nums[i])
                backtracking(nums, i+1)
                self.result.pop()

        nums.sort()
        backtracking(nums, 0)
        return self.results