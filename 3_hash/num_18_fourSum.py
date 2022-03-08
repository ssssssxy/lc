class Solution:
    def fourSum(self, nums, target: int):
        nums = sorted(nums)
        results = []

        if not nums or len(nums) < 4:
            return results

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in results:
                            results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif total >= target:
                        right -= 1
                    else:
                        left += 1
        return results


s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))