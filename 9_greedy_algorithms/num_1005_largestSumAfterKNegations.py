class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True) # 将A按绝对值从大到小排列
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        while k > 0:
            nums[-1] = -nums[-1]
            k -= 1
        return sum(nums)


s = Solution()
s.largestSumAfterKNegations([2,-3,-1,5,-4], 2)