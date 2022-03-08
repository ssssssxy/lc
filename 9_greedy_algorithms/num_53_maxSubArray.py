class Solution:
    def maxSubArray(self, nums) -> int:
        # 不能让“连续和”为负数的时候加上下一个元素，而不是不让“连续和”加上一个负数。
        max_sum = -float("inf")
        sum_ = 0
        for i in nums:
            sum_ += i
            if sum_ > max_sum:
                max_sum = sum_
            if sum_ <= 0:
                sum_ = 0

        return max_sum