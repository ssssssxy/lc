class Solution:
    def __init__(self):
        self.results = []
        self.result = []

    def permute(self, nums):

        def backtracking(nums, usage_list):
            if len(self.result) == len(nums):
                self.results.append(self.result[:])
                return

            for i in range(len(nums)):
                if usage_list[i]:
                    continue
                usage_list[i] = 1
                self.result.append(nums[i])
                backtracking(nums, usage_list)
                self.result.pop()
                usage_list[i] = 0

        usage_list = [0] * len(nums)
        backtracking(nums, usage_list)
        return self.results

s = Solution()
s.permute([1,2,3])