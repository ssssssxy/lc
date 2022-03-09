class Solution:
    def nextGreaterElements(self, nums):
        res = [-1] * len(nums)

        stack = []
        for i in range(len(nums) * 2):
            if not stack:
                stack.append(i % len(nums))
                continue

            if nums[i % len(nums)] <= nums[stack[-1]]:
                stack.append(i % len(nums))
            else:
                while stack and nums[i % len(nums)] > nums[stack[-1]]:
                    n = stack.pop()
                    res[n] = nums[i % len(nums)]
                stack.append(i % len(nums))
        return res
