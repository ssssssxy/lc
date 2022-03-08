class Solution:
    def __init__(self):
        self.results = []
        self.result = []


    def permuteUnique(self, nums):

        def backtracking(nums, usage_list):
            if len(self.result) == len(nums):
                self.results.append(self.result[:])

            for i in range(len(nums)):
                if usage_list[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not usage_list[i-1]:
                    continue
                usage_list[i] = 1
                self.result.append(nums[i])
                backtracking(nums, usage_list)
                self.result.pop()
                usage_list[i] = 0

        usage_list = [0] * len(nums)
        nums.sort()
        backtracking(nums, usage_list)
        return self.results

s = Solution()
s.permuteUnique([1,1,2])