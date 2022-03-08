class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        def at_most():
            ans = 0
            pre = 0
            for i in range(0, len(nums)):
                if nums[i] <= right:
                    pre += 1
                else:
                    pre = 0
                ans += pre
            return ans

        def at_min():
            ans = 0
            pre = 0
            for i in range(0, len(nums)):
                if nums[i] < left:
                    pre += 1
                else:
                    pre = 0
                ans += pre
            return ans

        r = at_most()
        l = at_min()
        return r - l

s = Solution()
print(s.numSubarrayBoundedMax([2,1,4,3], 2, 3))