class Solution:
    def threeSum(self, nums):
        results = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    if [nums[i], nums[left], nums[right]] not in results:
                        results.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return results

        return results

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))