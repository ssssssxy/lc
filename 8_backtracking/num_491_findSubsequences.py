class Solution:
    def __init__(self):
        self.results = []
        self.result = []

    def findSubsequences(self, nums):

        def backtracking(nums, start_index):
            if len(self.result) >= 2:
                self.results.append(self.result[:])
            if start_index == len(nums):
                return
            uasge_list = set()
            for i in range(start_index, len(nums)):
                if (len(self.result) >= 1 and nums[i] < self.result[-1]) or nums[i] in uasge_list:
                    continue
                uasge_list.add(nums[i])
                self.result.append(nums[i])
                backtracking(nums, i+1)
                self.result.pop()
                
        backtracking(nums, 0)
        return self.results

s = Solution()
print(s.findSubsequences([4,4,3,2,1]))