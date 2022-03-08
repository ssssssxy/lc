# class Solution:
#     def __init__(self):
#         self.results = []
#         self.result = []

#     def subsets(self, nums: List[int]) -> List[List[int]]:

#         def backtracking(nums, start_index):
#             self.results.append(self.result[:])
#             if start_index == len(nums):
#                 return
#             for i in range(start_index, len(nums)):
#                 if i > start_index and nums[i] == nums[i-1]:
#                     continue
#                 self.result.append(nums[i])
#                 backtracking(nums, i+1)
#                 self.result.pop()

#         nums.sort()
#         backtracking(nums, 0)
#         return self.results

class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def subsets(self, nums):
        self.paths.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index: int) -> None:
        # 收集子集，要先于终止判断
        self.paths.append(self.path[:])
        # Base Case
        if start_index == len(nums):
            return

        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()  # 回溯