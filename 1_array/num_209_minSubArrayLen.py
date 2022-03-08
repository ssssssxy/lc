class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        i = 0
        j = 1
        result = n+1
        while j <= n and i < j:
            if sum(nums[i:j]) >= target:
                if j - i < result:
                    result = j - i
                i += 1
            else:
                j += 1
        return result if result != n+1 else 0

s = Solution()
# print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))